import redis
r = redis.Redis(host='127.0.0.1',port=6379,db=0,password='123456')
u_list = r.keys('*') # 返回值列表

m_dict = {
    'user001:age':34,
    'user001:gender':'M',

}
r.mset(m_dict) # 参数是字典

print(r.get('user001:name')) # b'gds' # 返回值
print(r.mget('user001:age','user001:gender')) # 返回值列表 [b'34', b'M']