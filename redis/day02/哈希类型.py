import redis

r = redis.Redis(host='127.0.0.1',port=6379,db=0,password='123456')

# hset hget

r.hset('user1','name','fwl')
print(r.hget('user1','name'))

# hmset + hmget

user_dict = {
    'password':'123456',
    'gender':'M',
    'gf':'chuchu'
}
r.hmset('user1',user_dict)
print(r.hmget('user1','name','password','gender','gf'))

#hgetall + hkeysall + hvals
print(r.hgetall('user1'))
print(r.hkeys('user1'))
print(r.hvals('user1'))

# hdel
r.hdel('user1','gender','gf')
print(r.hgetall('user1'))
