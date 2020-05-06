import redis

r = redis.Redis(host='127.0.0.1',port=6379,db=0,password='123456')
# 常见端口号
# 1. mysql ->3306
# 2.mongodb ->27017
# 3.redis -> 6379
# 4.http ->80
# 5.http ->443
# 6.ssh ->22 远程链接服务
# 7.telnet ->23 远程链接服务
# ftp ->21

r.rpush('tedu:ts','dd','maria','cx')
r.rpush('tedu:ts','cc')

r.linsert('tedu:ts','after','maria','tao')
print(r.llen('tedu:ts'))
print(r.lrange('tedu:ts',0,-1))

# 弹出
print(r.rpop('tedu:ts'))
r.ltrim('tedu:ts',0,2)

while True:

    re = r.brpop('tedu:ts',3)
    if re:
        print(re)
    else:
        break
'''
(b'tedu:ts', b'tao') 元组类型
(b'tedu:ts', b'maria')
(b'tedu:ts', b'dd')
'''
r.expire('tedu:ts',10)

