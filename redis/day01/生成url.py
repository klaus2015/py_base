import random
import time

import redis

r = redis.Redis(host='localhost',port=6379,db=0,password='123456')

# 生产url

for page in range(67):
    url = 'http://app.mi.com/category/2#page={}'.format(page)
    r.lpush('xiaomi:spider',url)
    time.sleep(random.randint(1,3))

