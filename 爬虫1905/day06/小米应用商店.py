import requests
from threading import Thread
from queue import Queue
from fake_useragent import UserAgent
import time
from lxml import etree
import csv
from threading import Lock
class XMSpider:
    def __init__(self):
        self.url = 'http://app.mi.com/categotyAllListApi?page={}&categoryId={}&pageSize=30'
        self.q = Queue()
        self.f = open('xiaomi.csv','a')
        self.writer = csv.writer(self.f)
        # 创建线程锁 ,用于多个线程写入同一个文件
        self.lock = Lock()
    def get_useragent(self):
        ua = UserAgent()
        headers = {'User-Agent':ua.random}
        return headers

    def get_code(self):
        one_url = 'http://app.mi.com/category/13'
        html = requests.get(url=one_url,headers=self.get_useragent()).text
        # 解析
        parse_obj = etree.HTML(html)
        li_list = parse_obj.xpath('//ul[@class="category-list"]/li')

        for li in li_list:
            app_type = li.xpath('./a/text()')[0]
            app_code = li.xpath('./a/@href')[0].split('/')[-1]
            # 思考如何进行下去,需要什么数据?,url_in里面需要的页数,在这里提供
            app_total = self.get_app_total(app_code)
            # 调用入队列函数
            self.url_in(app_code,app_total)

    # 获取某个类别的总页数
    def get_app_total(self,app_code):
        url = self.url.format(1,app_code)
        html = requests.get(url=url,headers=self.get_useragent()).json()
        app_total = (html['count'] // 30) + 1
        return app_total


    def url_in(self,app_code,app_total):
        for page in range(0,app_total):
            url = self.url.format(page,app_code)
            self.q.put(url)

    def parse_html(self):
        while True:
            # 每抓取一页,将数据写入csv文件
            app_list = []
            if self.q.empty():
                break
            url = self.q.get()
            html = requests.get(url=url,headers=self.get_useragent()).json()
            for app in html['data']:
                name = app['displayName']
                link = 'http://app.mi.com/details?id=' + app['packageName']
                app_list.append((name,link))
            self.lock.acquire() # 多线程写入同一文件时记得枷锁,防止不确定因素
            self.writer.writerows(app_list)
            self.lock.release()




    def main(self):
        self.get_code()

        t_list = []
        for i in range(16):
            t = Thread(target=self.parse_html)
            t_list.append(t)
            t.start()

        for t in t_list:
            t.join()
        self.f.close()


if __name__ == '__main__':
    begin = time.time()
    xm = XMSpider()
    xm.main()

    end = time.time()
    print('运行时间:%.2f'%(end-begin))

"""
5:0.32
10:0.13
16:0.16
"""