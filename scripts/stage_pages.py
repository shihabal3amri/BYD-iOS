"""Stage the public site and an integrity-checked copy of its release IPA."""
import hashlib
import json
from pathlib import Path
import re
import shutil
import urllib.request

ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / '_site'
release = json.loads((ROOT / 'release.json').read_text())
tag, filename = release['release'], release['file']
assert re.fullmatch(r'v[0-9A-Za-z._-]+', tag)
assert re.fullmatch(r'[0-9A-Za-z._-]+\.ipa', filename)
assert not OUTPUT.exists(), 'Use a clean staging directory.'
OUTPUT.mkdir()
for name in ['index.html', 'source.json', 'release.json', '.nojekyll']:
    shutil.copy2(ROOT / name, OUTPUT / name)
shutil.copytree(ROOT / 'assets', OUTPUT / 'assets')

destination = OUTPUT / 'downloads' / tag / filename
destination.parent.mkdir(parents=True)
url = f'https://github.com/shihabal3amri/BYD-iOS/releases/download/{tag}/{filename}'
digest, size = hashlib.sha256(), 0
with urllib.request.urlopen(url, timeout=60) as response, destination.open('wb') as stream:
    while chunk := response.read(1024 * 1024):
        stream.write(chunk)
        digest.update(chunk)
        size += len(chunk)
assert size == release['bytes'], 'Release download size mismatch.'
assert digest.hexdigest() == release['sha256'], 'Release download checksum mismatch.'
assert sum(p.stat().st_size for p in OUTPUT.rglob('*') if p.is_file()) < 1_000_000_000
print(f'Staged site and verified IPA: {size} bytes, SHA256 {digest.hexdigest()}')
