
import pymysql
import hashlib

SALT = "#@Aid_"  # 加密用
class Database:
    def __init__(self,host='localhost',
                      port=3306,
                      user='root',
                      password='123456',
                      database = None,
                      charset='utf8'):
        self.host = host
        self.port = port
        self.user = user
        self.password = password
        self.database = database
        self.charset = charset
        self.connect_database()

    def connect_database(self):
        self.db = pymysql.connect(host=self.host,
                                  port=self.port,
                                  user=self.user,
                                  passwd=self.password,
                                  database=self.database,
                                  charset=self.charset)

    def close(self):
        self.db.close()

    def create_cursor(self):
        self.cur = self.db.cursor()   # 也可以在函数中添加属性 服务端需要用不同的游标调用同一个数据库


    # 注册操作
    def register(self,name,psw):
        sql = "select * from user where name='%s';"%name
        self.cur.execute(sql)
        if self.cur.fetchone():
            return False # 查找到返回True --不能重名
        # hash = hashlib.md5((name+SALT).encode()) # 加盐
        # hash.update(psw.encode()) # 算法加密
        # psw = hash.hexdigest() # 加密后的密码

        sql = "insert into user(name,psw) values('%s','%s');" % (name, psw)
        try:
            self.cur.execute(sql)
            self.db.commit()
            return True
        except Exception as e:
            self.db.rollback()
            return False

    # 登录操作
    def login(self,name,psw):
        sql = "select * from user where name='%s' and psw='%s'"%(name,psw)
        self.cur.execute(sql)
        if self.cur.fetchone():
            return True
        else:
            return False
    # 查单词
    def query(self,word):
        sql = "select expla from words where word='%s'"%word
        self.cur.execute(sql)
        r = self.cur.fetchone()
        if r:
            return r[0]
        # 没找到,不用处理,函数返回None

    # 插入历史
    def insert_hist(self,name,word):
        sql = "insert into hist (name,word) values (%s,%s)"
        try:
            self.cur.execute(sql,[name,word])
            self.db.commit()
        except Exception:
            self.db.rollback()

    # # 查询历史----我的
    # def do_history(self,name):
    #     sql = "select word from hist where name='%s' order by time desc limit 10"%name
    #     self.cur.execute(sql)
    #     r = self.cur.fetchall() # 返回形式元组套元组
    #     if r: # 数据库只管查询,不应该处理逻辑,函数任务的单一性
    #         return r
    #     else:
    #         return "没有历史记录"

    # 查询历史 --单一职责
    def do_history(self,name):
        sql = "select name,word,time from hist where name='%s' order by time desc limit 10"%name
        self.cur.execute(sql)
        return  self.cur.fetchall() # 返回形式元组套元组



