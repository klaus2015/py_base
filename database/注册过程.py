"""
  * 创建一个user表 包含 用户名和密码字段
     create table user (id int primary key auto_increment,name varchar(32) not null,passwd varchar(32) not null);
  应用程序中模拟注册和登录功能

     注册则输入用户名密码将用户名密码存入到数据库
     （用户名不能重复）

     登录则进行数据库比对，如果有该用户则打印登录成功
     否则让重新输入
"""


import pymysql


#链接数据库
db = pymysql.connect(host='localhost',
                     port=3306,
                     user='root',
                     password='123456',
                     database='grade',
                     charset='utf8')

# 获取游标  (操作数据库,执行sql语句)
cur = db.cursor()

def register():
    name = input("姓名: ")
    psw = input("请输入密码: ")
    sql = "select * from user where name='%s';"%name
    cur.execute(sql)
    if cur.fetchone():
        return False
    else:
        try:
            sql = "insert into user values('%s',%s);"%(name,psw)
            cur.execute(sql)
            db.commit()
            return True
        except Exception as e:
            db.rollback()
            print(e)
            return False
def login():
    name = input("姓名: ")
    psw = input("请输入密码: ")
    sql = "select * from user where name='%s' and psw = %s;"%(name,psw)
    cur.execute(sql)
    if cur.fetchone():
        return True

while True:
    print("""
            ================
            1.注册    2.登录
            ================
    """)
    cmd = input("请输入: ")
    if cmd == '1':
        if register():
            print("注册成功")
        else:
            print("注册失败")
    elif cmd == '2':
        if login():
            print("登录成功")
            break
        else:
            print("登录失败")

    else:
        print("做不到")

# 关闭数据库
cur.close()
db.close()

