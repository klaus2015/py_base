import requests
import time
from threading import Thread
from  queue import Queue
import json

class XiaomiSpider:
    def __init__(self):
        self.url = 'http://app.mi.com/categotyAllListApi?page={}&categoryId=2&pageSize=30'
        self.headers = {'User-Agent':'Mozilla/5.0'}
        self.url_queue = Queue()
        self.n = 0

    def in_queue(self):
        for i in range(7):
            url = self.url.format(i)
            self.url_queue.put(url)

    def get_data(self):
        while True:
            if self.url_queue.empty():
                break
            url = self.url_queue.get()
            res_str = requests.get(url,headers=self.headers).text
            res_json = json.loads(res_str)
            app_list = res_json['data']
            with open('xm007.json','a') as f:
                for app in app_list:
                    app_info = {}
                    app_info['name'] = app['displayName']
                    app_info['link'] = 'http://app.mi.com/details?id={}'.format(app['packageName'])
                    self.n += 1
                    json.dump(app_info,f,ensure_ascii=False)

    def main(self):
        t_list = []
        self.in_queue()
        for i in range(5):
            t = Thread(target=self.get_data)
            t_list.append(t)
            t.start()


        for t in t_list:
            t.join()

if __name__ == '__main__':
    start = time.time()
    spider = XiaomiSpider()
    spider.main()
    print(spider.n)
    end = time.time()
    print('执行时间:%.2f' % (end-start))