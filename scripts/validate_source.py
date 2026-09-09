"""Validate release metadata and, optionally, an actual downloadable IPA."""
import hashlib
import json
from pathlib import Path
import plistlib
import struct
import sys
from urllib.parse import urlparse
import zipfile

ROOT = Path(__file__).resolve().parents[1]
source = json.loads((ROOT / 'source.json').read_text())
release = json.loads((ROOT / 'release.json').read_text())
assert source['name'] and source['identifier']
assert len(source['apps']) == 1
app = source['apps'][0]
version = app['versions'][0]
assert app['bundleIdentifier'] == release['bundle_identifier_before_resigning']
assert version['version'] == release['base_version']
assert version['buildVersion'] == release['base_build']
assert version['size'] == release['bytes']
assert version['minOSVersion'] == release['minimum_ios']
assert len(release['sha256']) == 64
assert version['downloadURL'].endswith('/' + release['release'] + '/' + release['file'])
assert 'marketplaceID' not in app and 'patreon' not in app
assert all(isinstance(v, str) for v in app['appPermissions']['privacy'].values())
assert len(app['appPermissions']['entitlements']) == len(set(app['appPermissions']['entitlements']))
for url in [source['iconURL'], source['website'], app['iconURL'], version['downloadURL']] + app['screenshots']:
    assert urlparse(url).scheme == 'https' and urlparse(url).netloc
for url in [app['iconURL']] + app['screenshots']:
    path = ROOT / ('assets/' + url.rsplit('/', 1)[1])
    assert path.read_bytes().startswith(b'\x89PNG\r\n\x1a\n')


def get_entitlements(binary):
    assert struct.unpack_from('<I', binary)[0] == 0xFEEDFACF
    pos = 32
    for _ in range(struct.unpack_from('<I', binary, 16)[0]):
        cmd, length = struct.unpack_from('<II', binary, pos)
        if cmd == 0x1d:
            offset, size = struct.unpack_from('<II', binary, pos + 8)
            magic, total, count = struct.unpack_from('>III', binary, offset)
            assert magic == 0xfade0cc0 and total <= size
            for index in range(count):
                slot, relative = struct.unpack_from('>II', binary, offset + 12 + index * 8)
                if slot == 5:
                    start = offset + relative
                    blob_magic, blob_size = struct.unpack_from('>II', binary, start)
                    assert blob_magic == 0xfade7171
                    return plistlib.loads(binary[start+8:start+blob_size])
        pos += length
    raise AssertionError('No XML entitlements found in the main executable')


if len(sys.argv) > 1:
    ipa = Path(sys.argv[1])
    assert ipa.stat().st_size == version['size']
    assert hashlib.sha256(ipa.read_bytes()).hexdigest() == release['sha256']
    with zipfile.ZipFile(ipa) as archive:
        assert archive.testzip() is None
        assert all(n.startswith('Payload/') for n in archive.namelist())
        assert not any(n.endswith('.mobileprovision') or 'BYDAudit' in n for n in archive.namelist())
        info_path = next(n for n in archive.namelist() if n.count('/') == 2 and n.endswith('/Info.plist'))
        info = plistlib.loads(archive.read(info_path))
        assert info['CFBundleIdentifier'] == app['bundleIdentifier']
        assert info['CFBundleShortVersionString'] == version['version']
        assert info['CFBundleVersion'] == version['buildVersion']
        assert info['MinimumOSVersion'] == version['minOSVersion']
        assert 'UISupportedDevices' not in info
        assert {k for k in info if 'UsageDescription' in k} == set(app['appPermissions']['privacy'])
        binary = archive.read(info_path.rsplit('/', 1)[0] + '/' + info['CFBundleExecutable'])
        entitlements = get_entitlements(binary)
        assert set(entitlements) == set(app['appPermissions']['entitlements'])
        assert entitlements['com.apple.security.application-groups'] == ['group.com.byd.BYDi']
        # AltStore appends the same team suffix to the app and its declared groups.
        for team in ['ABCDEFGHIJ', '0123456789']:
            signed_id = info['CFBundleIdentifier'] + '.' + team
            signed_group = entitlements['com.apple.security.application-groups'][0] + '.' + team
            assert signed_group == 'group.' + signed_id
    print('PASS: IPA checksum, ZIP integrity, metadata, all permissions, and signing-group naming')
else:
    print('PASS: source metadata, URLs, permissions schema, and local images')
