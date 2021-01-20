# -*- coding: UTF-8 -*-
import requests
from http.server import BaseHTTPRequestHandler

def githubCI():
    r = requests.post("https://api.github.com/repos/Zfour/my-blog-source-file/dispatches",
    json = {"event_type": "run-it"},
    headers = {"User-Agent":'curl/7.52.1',
              'Content-Type': 'application/json',
              'Accept': 'application/vnd.github.everest-preview+json',
              'Authorization': 'token 8f3962d75da03fc8caed22d768741e092ce3ac1f'})
    if r.status_code == 204:
        return "This's OK!"
    else:
        return r.status_code

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        text = githubCI()
        text = str(text)
        self.send_response(200)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Content-type', 'text/plain')
        self.end_headers()
        self.wfile.write(text.encode())
        return
