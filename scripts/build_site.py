"""Render the three static GitHub Pages languages; --check detects stale output."""
import argparse
import html
from html import escape
import json
from pathlib import Path
from string import Template

ROOT = Path(__file__).resolve().parents[1]
LANGUAGES = {'en': 'English', 'ar': 'العربية', 'ru': 'Русский'}
SITE = 'https://shihabal3amri.github.io/BYD-iOS/'
REPO = 'https://github.com/shihabal3amri/BYD-iOS'



def render_supporters(items, content, prefix):
    esc = lambda value: html.escape(str(value), quote=True)
    cards = []
    for item in items:
        cards.append(f'''<li><a class="supporter" href="{esc(item['url'])}" target="_blank" rel="noopener noreferrer">
<img class="supporter-logo" src="{prefix}{esc(item['logo'])}" width="{item['width']}" height="{item['height']}" alt="{esc(item['name'])}" loading="lazy">
<div class="supporter-info"><span class="supporter-label">{esc(content['supporter_label'])}</span><h3><bdi dir="ltr">{esc(item['name'])}</bdi></h3></div>
<span class="supporter-follow">{esc(content['supporter_follow'])}<span aria-hidden="true">↗</span></span>
</a></li>''')
    return f'''<section class="supporters" id="supporters" aria-labelledby="supporters-heading">
<h2 id="supporters-heading">{esc(content['supporters_heading'])}</h2>
<p>{esc(content['supporters_intro'])}</p>
<ul class="supporter-list">{''.join(cards)}</ul>
</section>'''

def render_pages():
    template = Template((ROOT / 'content/page.html').read_text())
    source = json.loads((ROOT / 'source.json').read_text())
    version = source['apps'][0]['versions'][0]
    release = json.loads((ROOT / 'release.json').read_text())
    supporters = json.loads((ROOT / 'supporters.json').read_text(encoding='utf-8'))
    expected_keys = None
    for language in LANGUAGES:
        content = json.loads((ROOT / f'content/{language}.json').read_text())
        if expected_keys is None:
            expected_keys = set(content)
        assert set(content) == expected_keys, f'Translation keys differ: {language}'
        assert all(isinstance(value, str) and value.strip() for value in content.values())
        prefix = '' if language == 'en' else '../'
        page_path = '' if language == 'en' else f'{language}/'
        navigation = []
        for code, name in LANGUAGES.items():
            target = prefix + (f'{code}/' if code != 'en' else './')
            current = ' aria-current="page"' if code == language else ''
            navigation.append(f'<a href="{target}" lang="{code}" hreflang="{code}" dir="auto"{current}>{name}</a>')
        values = {
            key: value if key.endswith('_html') else escape(value, quote=True)
            for key, value in content.items()
        }
        values.update(
            supporters_html=render_supporters(supporters, content, prefix),
            lang=language, direction='rtl' if language == 'ar' else 'ltr', prefix=prefix,
            canonical=SITE + page_path, languages='\n        '.join(navigation),
            repo=REPO, release_url=f'{REPO}/releases/tag/{release["release"]}',
            readme_url=REPO + '/blob/main/README' + ('' if language == 'en' else f'.{language}') + '.md',
            download_url=escape(version['downloadURL'], quote=True),
            source_url='https://raw.githubusercontent.com/shihabal3amri/BYD-iOS/main/source.json',
        )
        yield ROOT / page_path / 'index.html', template.substitute(values)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--check', action='store_true')
    args = parser.parse_args()
    for path, rendered in render_pages():
        if args.check:
            assert path.exists() and path.read_text() == rendered, f'Rebuild with python3 scripts/build_site.py: {path}'
        else:
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(rendered)
    print('PASS: English, Arabic and Russian pages are current' if args.check else 'Built English, Arabic and Russian pages')
