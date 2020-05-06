import redis
import pymysql
r = redis.Redis(host='127.0.0.1',port=6379,db=0,password='123456')

db = pymysql.connect(host='localhost',password='123456',user='root',database='userdb',charset='utf8')
cursor = db.cursor()

# 1.输入查询的用户名
# 2. 先到redis中查询

# 3.redis中如果没有,到mysql中查询

username = input('输入: ')
re = r.hgetall(username)

if re:
    print('redis', re)
else:
    '''
    mysql 中查询 返回给用户
    缓存到reds中一份,过期时间30s'''
    sql = 'select age,gender,score from user where name=%s'
    cursor.execute(sql,[username])
    user_info = cursor.fetchall()
    if not user_info:
        print('不存在')
    else:
        user_dict = {
            'age':user_info[0][0],
            'gender':user_info[0][1],
            'score':user_info[0][2]
        }
        r.hmset(username,user_dict)
        r.expire(username,15)

        print('mysql:', user_info[0])

# 如果用户更改个人数据,在mysql修改后,一定要在redis里更新一下用户的缓存,即同步一下redis数据库

