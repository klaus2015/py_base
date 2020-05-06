import redis
import time
import random
from multiprocessing import Process

class Spider:
    def __init__(self):
        self.r = redis.Redis(host='localhost', port=6379, db=0, password='123456')

    # 生产者进程事件
    def product(self):
        for page in range(67):
            url = 'http://app.mi.com/category/2#page={}'.format(page)
            self.r.lpush('xiaomi:spider', url)
            time.sleep(random.randint(1, 3))

    # 消费者
    def consumer(self):
        while True:
            url = self.r.brpop('xiaomi:spider', 4)
            if url:
                print('正则抓取', url[1].decode())
            else:
                print('抓取结束')
                break

    def run(self):
        p1 = Process(target=self.product)
        p2 = Process(target=self.consumer)
        p1.start()
        p2.start()
        p1.join()
        p2.join()
if __name__ == '__main__':
    s = Spider()
    s.run()