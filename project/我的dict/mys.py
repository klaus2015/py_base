import pymysql

db = pymysql.connect(host='localhost',
                     port=3306,
                     user='root',
                     password='123456',
                     database='grade',
                     charset='utf8')

cur = db.cursor()
def register(name,psw):
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
# def login():
#     name = input("姓名: ")
#     psw = input("请输入密码: ")
#     sql = "select * from user where name='%s' and psw = %s;"%(name,psw)
#     cur.execute(sql)
#     if cur.fetchone():
#         return True

# 关闭数据库
# cur.close()
# db.close()