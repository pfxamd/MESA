"""Fast deterministic checks of generated routes, media and authored data."""
from pathlib import Path
import json,re,sys,hashlib
ROOT=Path(__file__).resolve().parents[1]
recipes=json.loads((ROOT/'content/recipes.json').read_text(encoding='utf8'))
stories=json.loads((ROOT/'content/stories.json').read_text(encoding='utf8'))
images=json.loads((ROOT/'data/images.json').read_text(encoding='utf8'))['images']
docs=ROOT/'dist'
checks=[]
def check(condition,msg):
 checks.append((bool(condition),msg))
 if not condition:print('FAIL:',msg)
check(len(recipes)==12,'12 authored recipes')
check(len(stories)==4,'4 authored stories')
check(len(images)==36,'36 indexed photographs')
check(len(set(r['slug'] for r in recipes))==12,'Unique recipe slugs')
check(len(set(s['slug'] for s in stories))==4,'Unique story slugs')
check((docs/'index.html').exists(),'Homepage output')
expected=['recipes','kitchen','stories','about']+['recipes/'+r['slug'] for r in recipes]+['stories/'+s['slug'] for s in stories]
for p in expected:check((docs/p/'index.html').exists(),'Page exists '+p)
image_paths={img['src'] for img in images}
for img in images:
 p=ROOT/'public'/img['src'].lstrip('/')
 check(p.exists(), 'Image exists '+str(img['id']))
 if p.exists():check(hashlib.sha256(p.read_bytes()).hexdigest()==img['sha256'],'Checksum image '+str(img['id']))
for r in recipes:
 check(r['hero'] in image_paths,'Hero linked '+r['slug'])
 check(r['process'] in image_paths,'Process linked '+r['slug'])
 check(len(r['steps'])>=4,'Method steps '+r['slug'])
 check(len(r['ingredients'])>=6,'Ingredient details '+r['slug'])
for page in [docs/'index.html']+[docs/p/'index.html' for p in expected]:
 text=page.read_text(encoding='utf8')
 check('<main id="main">' in text and '</main>' in text,'Main landmark '+str(page.relative_to(docs)))
 check('www.pfxamd.com' in text,'Credit '+str(page.relative_to(docs)))
 # Collect site-local absolute paths only (do not misread DOM attributes as paths)
 for match in re.findall(r'(?:src|href)="(/MESA/[^"?#]*)',text):
  dest=docs/match[len('/MESA/'):]
  if match.endswith('/'):dest=dest/'index.html'
  check(dest.exists(),'Link '+match+' on '+str(page.relative_to(docs)))
print('MESA checks:',sum(ok for ok,msg in checks),'/',len(checks),'passed')
sys.exit(0 if all(ok for ok,msg in checks) else 1)
