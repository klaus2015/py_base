import redis
import json

r = redis.Redis(host='127.0.0.1',port=6379,db=0,password='123456')

# 列表
key_list = r.keys('*')
for k in key_list:
    print(k.decode())

print(r.type('mylist')) # b'list'

print(r.exists('mylist')) # 1

r.expire('mylist',5)