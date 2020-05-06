import requests
import time
from multiprocessing import Process
from  queue import Queue
import json

class XiaomiSpider:
    def __init__(self):
        self.url = 'http://app.mi.com/categotyAllListApi?page={}&categoryId=2&pageSize=30'
        self.headers = {'User-Agent':'Mozilla/5.0'}
        self.url_queue = Queue()
        self.n = 0
    #
    def url_in(self):
        for i in range(10):
            url = self.url.format(i)
            self.url_queue.put(url)

    # 线程时间函数
    def get_data(self):
        while True:
            if self.url_queue.empty():
                break
            # 获取地址,请求 + 解析+ 保存
            url = self.url_queue.get()
            html = requests.get(url=url,headers=self.headers).content.decode('utf-8')
            html = json.loads(html)
            with open('XXX2.json', 'a') as f:

                app_dict = {}
                for app in html['data']:
                    app_dict['app_name'] = app['displayName']
                    app_dict['app_link'] = 'http://app.mi.com/details?id=' + app['packageName']
                    json.dump(app_dict, f, ensure_ascii=False)
                    self.n += 1

    #
    def main(self):

            # url入队列
            self.url_in()
            # 创建多线程
            t_list = []
            for i in range(5):
                t = Process(target=self.get_data)
                t_list.append(t)
                t.start()
            for i in t_list:
                i.join()


            print(self.n)



if __name__ == '__main__':
    start = time.time()
    spider = XiaomiSpider()
    spider.main()
    end = time.time()
    print('执行时间:%.2f' % (end-start))