#!/usr/bin/env python3
from http.server import ThreadingHTTPServer,SimpleHTTPRequestHandler
from pathlib import Path
from urllib.parse import urlsplit
import os
ROOT=Path(__file__).resolve().parent/'docs'
BASE=os.environ.get('MESA_BASE','/MESA').rstrip('/')
class Handler(SimpleHTTPRequestHandler):
 def translate_path(self,path):
  url=urlsplit(path).path
  if not (url==BASE or url.startswith(BASE+'/')):return '/__not_found__'
  rel=url[len(BASE):].lstrip('/')
  return str(ROOT/rel)
 def log_message(self,*args):pass
 def do_GET(self):
  if not (urlsplit(self.path).path==BASE or urlsplit(self.path).path.startswith(BASE+'/')):
   self.send_error(404);return
  super().do_GET()
if __name__=='__main__':
 port=int(os.environ.get('PORT','8075'))
 print(f'MESA preview: http://127.0.0.1:{port}{BASE}/',flush=True)
 ThreadingHTTPServer(('127.0.0.1',port),Handler).serve_forever()
