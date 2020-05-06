import redis

r = redis.Redis(host='127.0.0.1',port=6379,db=0,password='123456')

# user:001  一年中第五天和第200天登录
r.setbit('user:001',4,1)
r.setbit('user:001',199,1)
# user:002
r.setbit('user:002',99,1)
r.setbit('user:002',299,1)

# user:003 登录100次以上
for i in range(0,366,2):
    r.setbit('user:003',i,1)

# print(r.bitcount('user:003'))


# user:004 登录100次以上
for i in range(0,366,3):
    r.setbit('user:004',i,1)

u_list = r.keys('*')

active_users = []
noactive_users= []
for user in u_list:
    login_count = r.bitcount(user)
    if login_count >= 100:
        active_users.append((user,login_count))
    else:
        noactive_users.append((user,login_count))

print(active_users)
print(noactive_users)