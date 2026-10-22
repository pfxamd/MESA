"""Publish verified central media URLs and omit generated duplicate copies."""
import hashlib,json,re
from pathlib import Path

def publish_media(root):
    root=Path(root).resolve()
    manifest=json.loads((root/'media/manifest.json').read_text(encoding='utf-8-sig'))
    verified=json.loads((root/'media/verification.json').read_text(encoding='utf-8-sig'))
    out=root/'dist'
    records=manifest['records']
    if len(records)!=37 or len(verified)!=37:
        raise ValueError('Incomplete verified media manifest')
    for row in records:
        relative=Path(row['output'])
        if relative.is_absolute() or '..' in relative.parts or not row['key'].startswith(manifest['prefix']):
            raise ValueError('Unsafe media path')
        data=(root/row['source']).read_bytes()
        if relative.suffix=='.svg':
            data=data.replace(b'\r\n',b'\n')
        if hashlib.sha256(data).hexdigest()!=row['sha256']:
            raise ValueError('Original changed; upload and verify first: '+row['source'])
        if not any(v['key']==row['key'] and v['verified'] and v['sha256']==row['sha256'] and v['bytes']==row['bytes'] for v in verified):
            raise ValueError('Unverified R2 file: '+row['key'])
        if not (out/relative).is_file():
            raise ValueError('Missing generated media: '+row['output'])
    pending=[]
    for file in out.rglob('*'):
        if file.suffix not in ('.html','.css','.js'):
            continue
        original=file.read_text(encoding='utf-8')
        text=original
        for row in records:
            text=re.sub(r'(?:https://pfxamd\.github\.io/MESA/|/MESA/|(?:\.\./)*(?:\./)?)'+re.escape(row['output']), 'https://media.pfxamd.com/'+row['key'],text)
        if re.search(r'(?:\.\./)*assets/images/[^\s\"\'<>]+\.(?:webp|png|jpg|avif)',text):
            raise ValueError('Unmapped media reference: '+str(file))
        if text!=original:
            pending.append((file,text))
    for file,text in pending:
        file.write_text(text,encoding='utf-8',newline='')
    for row in records:
        (out/row['output']).unlink()
    (out/'assets/image-manifest.json').unlink(missing_ok=True)
    for directory in sorted(out.rglob('*'),key=lambda p:len(p.parts),reverse=True):
        if directory.is_dir() and not any(directory.iterdir()):
            directory.rmdir()
    print('R2 publication:',len(records),'verified original files excluded from dist')
