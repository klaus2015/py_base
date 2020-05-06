import redis

r = redis.Redis(host='localhost',port=6379,db=0,password='123456')

day01_dict = {
    'hw':5000,
    'oppo':4000,
    'iphone':3000
}
day02_dict = {
    'hw':5200,
    'oppo':4200,
    'iphone':3200
}
day03_dict = {
    'hw':5400,
    'oppo':4300,
    'iphone':3600
}
r.zadd('m:01',day01_dict)
r.zadd('m:02',day02_dict)
r.zadd('m:03',day03_dict)

r.zunionstore('m:01-03',('m:01','m:02','m:03'),aggregate='max')
res_list = r.zrevrange('m:01-03',0,-1,withscores=True)
i = 1
for re in res_list:
    print('第{}名:{}销量{}'.format(i,re[0].decode(),re[1]))
    i += 1