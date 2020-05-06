import redis


r = redis.Redis(host='127.0.0.1',port=6379,db=0,password='123456')

# python 操作集合

# 添加
r.sadd('mysite10','A','B')
print(r.smembers('mysite10')) # 返回值类型{b'B', b'A'} 集合
print(r.scard('mysite10')) # 2

# ismember
print(r.sismember('mysite10','A')) # True

# 交集 + 并集
r.sadd('mysite11','A','B','C')
r.sadd('mysite12','B','C','D')
print(r.sinter('mysite10','mysite11','mysite12')) # {b'B'}
print(r.sunion('mysite10','mysite11','mysite12')) # {b'B', b'A', b'C', b'D'}

res = r.sunion('mysite10','mysite11','mysite12')
set_1 = set()
for re in res:
    set_1.add(re.decode())
