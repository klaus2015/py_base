import requests
import json
from fake_useragent import UserAgent
import time
import random
import re
class DoubanSpider(object):
    def __init__(self):
        self.url = 'https://movie.douban.com/j/chart/top_list?' \
                   'type={}&interval_id=100%3A90&action=&' \
                   'start={}&limit=20'
        self.n = 0
        # 正则批量处理headers
        # 1. Pycharm中,Ctrl+r,选中　Regex
        # (.*): (.*)
        # '$1': '$2',
        # 点击Replace All

    def get_headers(self):
        ua = UserAgent()
        headers = {'User-Agent':ua.random}
        return headers

    def get_html(self,url):
        html = requests.get(url=url,headers=self.get_headers()).text
        return html

    def parse_html(self,url):
        html_json = json.loads(self.get_html(url))
        for one_film in html_json:
            name = one_film['title']
            score = one_film['score']
            print(name,score)
            self.n += 1

    def get_total(self,type_code):
        url = 'https://movie.douban.com/j/chart/top_list_count?type={}&interval_id=100%3A90'.format(type_code)
        html = self.get_html(url)
        html = json.loads(html)
        total = html['total']

        return total

    def get_code(self,name):
        url = 'https://movie.douban.com/chart'
        html = self.get_html(url)
        re_bds = '<a href="/typerank.*?type=(.*?)&.*?>(.*?)</a>'
        pattern  = re.compile(re_bds,re.S)
        # r_list :[('11','剧情'),('13','爱情')]
        r_list = pattern.findall(html)
        item = {}
        menu = ''
        for r in r_list:
            item[r[1]] = r[0]
            menu = menu + r[1] + '|'
        type_code = item.get(name)
        return type_code,menu

    def main(self):
        while True:
            type_code, menu = self.get_code('剧情')
            name = input(menu + '\n' + "请输入要抓取的电影类别: ")
            # 通过用户输入,查找对应的类型码
            type_code,menu = self.get_code(name)
            # 根据类型码计算总数
            if not type_code:
                continue

            else:
                total = self.get_total(type_code)
                for start in range(0,total,20):
                    url = self.url.format(type_code,start)
                    self.parse_html(url)
                    time.sleep(random.randint(1,3))
                print('总数:%s'%self.n)

if __name__ == '__main__':
    d = DoubanSpider()
    d.main()

