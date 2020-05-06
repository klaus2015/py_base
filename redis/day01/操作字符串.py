import redis

r = redis.Redis(host='localhost',port=6379,db=0,password='123456')

r.set('user001:name','gds')

m_dict = {
    'user001:age':34,
    'user001:gender':'M',

}
r.mset(m_dict)

print(r.get('user001:name')) # b'gds'
print(r.mget('user001:age','user001:gender')) # 返回值列表 [b'34', b'M']

print(r.strlen('user001:name')) # 3

# 数值类型操作
r.incr('user001:age',1)
r.decr('user001:age',1)
r.incrby('user001:age',3)
r.decrby('user001:age',3)

r.incrbyfloat('user001:age',1.5)
r.incrbyfloat('user001:age',-1.5)
