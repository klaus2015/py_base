import requests
from ydmapi import get_result
from lxml import etree
from urllib.request import urlretrieve
class AttackYdm:
    def __init__(self):
        self.url = 'http://www.yundama.com/'
        self.headers = {
            'User-Agent':'Mozilla/5.0'
        }


    # 获取验证码截图
    def get_index(self):
        html = requests.get(url=self.url,headers=self.headers).text
        parse_obj = etree.HTML(html)
        # 验证码链接地址
        captcha = parse_obj.xpath('//*[@id="verifyImg"]/@src')
        captcha = 'http://www.yundama.com' + captcha[0]
        urlretrieve(captcha,filename='000000.png')

if __name__ == '__main__':
    a = AttackYdm()
    a.get_index()