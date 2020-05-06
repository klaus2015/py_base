

from urllib import request
import time
import re
import pymongo
import random

class MaoyanSpider(object):
    def __init__(self):
        self.url = 'https://maoyan.com/board/4?offset={}'
        self.ua_list = [
            'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/14.0.835.163 Safari/535.1',
            'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:6.0) Gecko/20100101 Firefox/6.0',
            'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; InfoPath.3)'
        ]
        # 用于记录页数
        self.page = 1
        # 创建数据库连接对象和游标对象
        self.conn = pymongo.MongoClient('localhost',27017)
        self.db = self.conn['maoy']
        self.myset = self.db['filmtab']


    # 获取
    def get_page(self,url):
        # 每次使用随机的user-agent
        headers = {'User-Agent':random.choice(self.ua_list)}
        req = request.Request(
            url=url,
            headers=headers
        )
        res = request.urlopen(req)
        html = res.read().decode('utf-8')
        # 直接调用解析函数
        self.parse_page(html)

    # 解析
    def parse_page(self,html):
        pattren = re.compile('<div class="movie-item-info">.*?title="(.*?)".*?class="star">(.*?)</p>.*?releasetime">(.*?)</p>',re.S)
        # rlist: [('霸王别姬','张国荣','1993'),(),()]
        r_list = pattren.findall(html)
        print(r_list)
        self.write_page(r_list)

    # 存入mongo数据库
    def write_page(self,r_list):

        # 处理数据,放到大列表film_list中
        for rt in r_list:
            # 定义空字典
            item = {}
            item['name'] = rt[0]
            item['star'] = rt[1]
            item['time'] = rt[2].strip()[5:15]
            self.myset.insert_one(item)

    def main(self):
        for offset in range(0,91,10):
            url = self.url.format(offset)
            self.get_page(url)
            time.sleep(random.randint(1,3))
            print('第%d页爬取完成' % self.page)
            self.page += 1




if __name__ == '__main__':
    start = time.time()
    spider = MaoyanSpider()
    spider.main()
    end = time.time()
    print('执行时间: %.2f' % (end-start))