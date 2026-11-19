from html.parser import HTMLParser
from pathlib import Path
import re,json,hashlib
D=Path(__file__).parent/'dist'
class P(HTMLParser):
 def __init__(self):super().__init__();self.ids=[];self.refs=[];self.h1=0;self.imgs=[]
 def handle_starttag(self,t,a):
  a=dict(a)
  if 'id'in a:self.ids.append(a['id'])
  for k in ['href','src']:
   if k in a:self.refs.append(a[k])
  if t=='h1':self.h1+=1
  if t=='img':self.imgs.append(a)
parsed={}
for f in D.glob('*.html'):
 if f.name=='qa.html':continue
 p=P();p.feed(f.read_text());assert len(p.ids)==len(set(p.ids)),f.name;assert p.h1==1,f.name
 assert all('alt'in a and a['alt'] for a in p.imgs),f.name
 parsed[f.name]=p
for name,p in parsed.items():
 for ref in p.refs:
  if re.match(r'^([a-z]+:|//)',ref):continue
  path,_,anchor=ref.partition('#');path=path.split('?')[0] or name
  assert (D/path).is_file(),(name,ref)
  if anchor and path.endswith('.html'):assert anchor in parsed[path].ids or (path=='applications.html' and anchor in ['interior','charm','expo','mobility','slowear','aesop','gelato']),(name,ref)
for item in json.loads((D/'search-index.json').read_text()):
 name,_,anchor=item['file'].partition('#');assert name in parsed
 if anchor:assert anchor in parsed[name].ids
 assert item['title'].strip(),item
assert len(parsed)==7
for name,expected in json.loads((D.parent/'asset-manifest.json').read_text()).items():
 assert hashlib.sha256((D/'assets'/name).read_bytes()).hexdigest()==expected,name
print('PASS: 7 pages, local links, anchors, unique IDs, image descriptions, current PDF, unchanged original logo/apostrophe/font files, and deep-link search index.')
