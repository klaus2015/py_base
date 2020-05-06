"""
数据库  写操作---insert / update / delete
"""

import pymysql

#链接数据库
db = pymysql.connect(host='localhost',
                     port=3306,
                     user='root',
                     password='123456',
                     database='stu',
                     charset='utf8')

# 获取游标  (操作数据库,执行sql语句)
cur = db.cursor()

# 写入数据库
try:  # 写入操作有可能出错,加try-except捕获错误,保证数据库的完整性
    # name = input("Name:")
    # age = input("Age:")
    # score = input("Score")
    # 将变量插入到sql语句合成最终操作语句
    # sql = "insert into class_1 (name,age,score) values('%s',%s,%s);"%(name,age,score) # 方法1
    # cur.execute(sql)

    # sql = "insert into class_1 (name,age,score) values(%s,%s,%s);" # 传参方法2
    # # 可以使用列表直接给sql语句的values 传值
    # cur.execute(sql,[name,age,score])# --此处列表只能给values后的参数传值

    # 修改操作
    # sql = "update interest set price=1180 where name='Abby'"
    # cur.execute(sql)

    # 删除操作
    sql = "delete from class_1 where name='Zxm'"
    cur.execute(sql)

    db.commit()
except Exception as e:
    db.rollback() # 退回到commit执行之前的数据库状态
    print(e)




# 关闭数据库
cur.close()
db.close()
