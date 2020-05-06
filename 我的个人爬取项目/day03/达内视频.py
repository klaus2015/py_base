import requests
from lxml import etree


class DNSpider:
    def __init__(self):
        self.post_url = 'http://uc.tmooc.cn/login'
        self.url1 = 'http://uc.tmooc.cn/userCenter/toUserSingUpCoursePage'
        self.url = 'http://videotts.it211.com.cn/aid19050906pm/aid19050906pm.m3u8'
        self.session = requests.session()
        self.headers = {
            "Origin": "http://www.tmooc.cn",
            "Referer": "http://www.tmooc.cn/",
            "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.75 Safari/537.36",
        }

    def get_html(self):
        data = {
            "loginName": "598467866@qq.com",
            "password": "bc08abbeed0ff1bd7d8ea7ddc10fa393",
            # "accountType": "1",
        }

        resp = self.session.post(url=self.post_url, data=data, headers=self.headers)
        print(resp.status_code)
        print(resp.text)




if __name__ == '__main__':
    d = DNSpider()
    d.get_html()
