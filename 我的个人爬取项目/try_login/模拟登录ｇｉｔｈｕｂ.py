import re

import requests
from lxml import etree
class GithubLogin(object):
    def __init__(self,email, pwd):
        self.headers = {
            'Referer': 'https://github.com/',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',
            'Host': 'github.com'
        }
        self.login_url = 'https://github.com/login'
        self.post_url = 'https://github.com/session'
        self.logined_url = 'https://github.com/settings/profile'
        self.session = requests.session()
        self.email = email
        self.pwd = pwd
    def login_github(self):
        data = {
            "commit": "Sign in",
            "utf8": "✓",
            "authenticity_token": self.get_token(),
            "login": self.email,
            "password": self.pwd
        }
        resp = self.session.post(self.post_url,data=data,headers=self.headers)
        print('StatusCode:', resp.status_code)
        if resp.status_code != 200:
            print('Login Fail')
        else:
            match = re.search(r'"user-login" content="(.*?)"', resp.text)
            user_name = match.group(1)
            print('UserName:', user_name)
            print(resp.text)


    def get_token(self):
        resp = self.session.get(self.login_url, headers=self.headers)
        if resp.status_code != 200:
            print("Fail to login")
            return None
        match = re.search(r'name="authenticity_token" value="(.*?)" />',resp.text)
        if not match:
            print('Get Token Fail')
            return None

        return match.group(1)

if __name__ == '__main__':
    email = input('Account:')
    password = input('Password:')
    l = GithubLogin(email,password)
    l.login_github()
    print(l.get_token())