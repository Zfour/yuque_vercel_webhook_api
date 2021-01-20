# -*- coding: UTF-8 -*-
import requests
from http.server import BaseHTTPRequestHandler

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        r = requests.post("https://api.github.com/repos/Zfour/my-blog-source-file/dispatches",
        json = {"event_type": "run-it"},
        headers = {"User-Agent":'curl/7.52.1',
              'Content-Type': 'application/json',
              'Accept': 'application/vnd.github.everest-preview+json',
              'Authorization': 'token 36d615c7ae1614a74c89ff2bb49842da5b5c382a'})
        text = str(r)
        self.send_response(200)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Content-type', 'text/plain')
        self.end_headers()
        self.wfile.write(text.encode())
        return
