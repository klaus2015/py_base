import redis
import pymysql
# 如果用户更改个人数据,在mysql修改后,一定要在redis里更新一下用户的缓存,即同步一下redis数据库
# 跟新mysql
class Update:
    def __init__(self):
        self.db = pymysql.connect(host='localhost',password='123456',user='root',database='userdb',charset='utf8')
        self.r = redis.Redis(host='127.0.0.1',port=6379,db=0,password='123456')
        self.cursor = self.db.cursor()

    def update_mysql(self,username, score):
        sql = 'update user set score=%s where name=%s'
        try:
            code = self.cursor.execute(sql, [score, username])
            if code == 1:
                self.db.commit()
                return True
        except Exception as e:
            self.db.rollback()
            print(e)


    def update_redis(self,username, score):
        result = self.r.hgetall(username)
        # 存在, 只更新score 否则缓存整个用户信息
        if result:
            self.r.hset(username,'score',score)
        else:
            self.select_mysql(username)

    def select_mysql(self,username):
        sql = 'select age,gender,score from user where name=%s'
        self.cursor.execute(sql, [username])
        user_info = self.cursor.fetchall()
        user_dict = {
            'age': user_info[0][0],
            'gender': user_info[0][1],
            'score': user_info[0][2]
        }
        self.r.hmset(username, user_dict)
        self.r.expire(username, 60)

    def main(self):
        username = input('name: ')
        new_score = input('score: ')
        if self.update_mysql(username,new_score):
            self.update_redis(username,new_score)
        else:
            print('更改失败')
if __name__ == '__main__':
    syn = Update()
    syn.main()