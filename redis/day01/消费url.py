import redis

r = redis.Redis(host='localhost',port=6379,db=0,password='123456')

while True:
    url = r.brpop('xiaomi:spider',4)
    if url:
        print('正则抓取',url[1].decode())
    else:
        print('抓取结束')
        break

