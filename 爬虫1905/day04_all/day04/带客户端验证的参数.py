import requests
from lxml import etree
from fake_useragent import UserAgent
import os

class CodeSpider:
    def __init__(self):
        self.url = 'http://code.tarena.com.cn/AIDCode/aid1905/13_redis/'
        self.auth = ('tarenacode','code_2013')

    def ran_useragent(self):
        ua = UserAgent()
        headers = {'User-Agent':ua.random}
        return headers

    def get_html(self):
        html = requests.get(url=self.url,auth=self.auth,headers=self.ran_useragent()).text
        parse_obj = etree.HTML(html)
        href_list = parse_obj.xpath('//a/@href')
        for href in href_list:
            if href.endswith('.zip') or href.endswith('.rar'):
                self.save_file(href)

    def save_file(self,href):
        # href = redis_day01.zip
        base_directory = '/home/tarena/code/'
        directory = base_directory + '/'.join(self.url.split('/')[3:-1]) + '/'
        if not os.path.exists(base_directory):
            os.makedirs(directory)
        file_url = self.url + href
        html = requests.get(url=file_url,auth=self.auth,headers=self.ran_useragent()).content
        filename = directory + href
        with open(filename,'wb') as f:
            f.write(html)
        print("下载完成")

    def main(self):
        self.get_html()

c = CodeSpider()
c.main()