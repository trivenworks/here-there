"""Vercel request adapters; credentials never go to browser responses or logs."""
from urllib.parse import urlsplit
import json,os,re

def reply(request,status,payload):
 data=json.dumps(payload,ensure_ascii=False).encode('utf-8')
 request.send_response(status);request.send_header('Content-Type','application/json; charset=utf-8');request.send_header('Cache-Control','no-store');request.send_header('X-Content-Type-Options','nosniff');request.send_header('Content-Length',str(len(data)));request.end_headers();request.wfile.write(data)

def same_origin(request):
 host=(request.headers.get('X-Forwarded-Host') or request.headers.get('Host') or '').split(',')[0].strip().lower()
 origin=request.headers.get('Origin');site=request.headers.get('Sec-Fetch-Site','')
 if site=='cross-site' or (origin and urlsplit(origin).netloc.lower()!=host):
  reply(request,403,{'code':'SAME_ORIGIN_ONLY','message':'같은 웹사이트에서만 요청할 수 있습니다.'});return False
 return True

def map_config(request):
 if not same_origin(request):return
 key=os.environ.get('NAVER_MAP_CLIENT_ID','').strip()
 if key and not re.fullmatch(r'[A-Za-z0-9_-]+',key):key=''
 reply(request,200,{'map_client_id':key})
