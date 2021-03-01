# -*- coding: UTF-8 -*-
import requests
import re
from http.server import BaseHTTPRequestHandler
from bs4 import BeautifulSoup

def github_json(user,repo):
    requests_path = 'https://github.com/' + user + '/' +repo + '/blob/master/friendlist.json'
    gitpage = requests.get(requests_path).text
    soup = BeautifulSoup(gitpage, 'html.parser')
    main_content = soup.find('td',id = 'LC1').text
    print(main_content)

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        path = self.path
        path = path.replace("'", '"')
        repo_reg = re.compile(r'repo="(.*?)"')
        user_reg = re.compile(r'user="(.*?)"')
        user = user_reg.findall(path)[0]
        repo = repo_reg.findall(path)[0]
        data = github_json(user,repo)
        self.send_response(200)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Content-type', 'text/plain')
        self.end_headers()
        self.wfile.write(json.dumps(data).encode('utf-8'))
        return