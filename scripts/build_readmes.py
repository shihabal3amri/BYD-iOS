"""Generate five current installation guides from the same reviewed page text."""
from pathlib import Path
import re,json,html
ROOT=Path(__file__).resolve().parents[1]
def md(s):
 s=re.sub(r'<a href="([^"]+)">(.*?)</a>',lambda m:'['+m[2]+']('+m[1]+')',s)
 s=s.replace('<strong>','**').replace('</strong>','**').replace('<br>','\n')
 return html.unescape(re.sub(r'<[^>]+>','',s))
def main():
 release=json.loads((ROOT/'release.json').read_text());url='https://github.com/shihabal3amri/BYD-iOS/releases/tag/'+release['release']
 for lang in ['en','ar','ru','es','zh-Hans']:
  c=json.loads((ROOT/f'content/{lang}.json').read_text());site='https://shihabal3amri.github.io/BYD-iOS/'+('' if lang=='en' else lang+'/')
  parts=['# '+c['title'],md(c['intro_html']),f"[{c['download']}]({site}) · [{c['release_link']}]({url})",'## '+c['widgets_heading'],md(c['widgets_intro_html']),md(c['widgets_install_html']),md(c['widgets_ids_html']),'## '+c['setup_heading'],md(c['setup_intro_html']),f"[{c['mac_guide']}](https://faq.altstore.io/altstore-classic/how-to-install-altstore-macos) · [{c['windows_guide']}](https://faq.altstore.io/altstore-classic/how-to-install-altstore-windows)",'## '+c['install_heading']]
  parts+=['\n'.join(f'{i}. '+md(c[k]) for i,k in enumerate(['install_one_html','install_two_html','install_three_html'],1)),md(c['update_html']),md(c['refresh_html']),md(c['source_label_html']),'`https://raw.githubusercontent.com/shihabal3amri/BYD-iOS/main/source.json`','## '+c['impactor_heading'],md(c['impactor_html']),md(c['impactor_note_html']),'## '+c['walkup_heading'],md(c['walkup_intro_html'])]
  parts+=['\n'.join(f'{i}. '+md(c[k]) for i,k in enumerate(['walkup_one_html','walkup_two_html','walkup_three_html'],1)),c['walkup_background'],md(c['walkup_issue_html']),c['walkup_logs'],'## '+c['status_heading'],c['status_text'],c['status_note'],'## '+c['release_link'],f"`{release['file']}`\n\nSHA-256: `{release['sha256']}`",'## '+c['telegram_heading'],c['telegram_intro'],f"[{c['telegram_subscribe']}](https://t.me/byd_localized)",c['footer_text']]
  filename='README'+('' if lang=='en' else '.'+lang)+'.md';(ROOT/filename).write_text('\n\n'.join(parts)+'\n')
if __name__=='__main__':main()
