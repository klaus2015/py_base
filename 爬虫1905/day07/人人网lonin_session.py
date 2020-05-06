
import requests
import re


'http://www.renren.com/PLogin.do'


class Renrenlogin:
    def __init__(self):
        self.url = 'http://www.renren.com/972102637/profile'
        self.post_url = 'http://www.renren.com/PLogin.do'
        self.headers = {
            "Referer": "http://www.renren.com/972102637/profile",

            "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.75 Safari/537.36"
        }
        self.session = requests.session()

    def parse_html(self):
        data = {'email': '13067906601', 'password': 'zxm153113'}

        res = self.session.post(url=self.post_url, data=data, headers=self.headers)
        html = self.session.get(url=self.url, headers=self.headers)
        print(res)
        print(html)

x = Renrenlogin()
x.parse_html()