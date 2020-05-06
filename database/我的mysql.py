"""
mysql数据库
数据库基本流程演示
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

# 执行sql语句
sql = "insert into class_1 values(6,'Selina',19,'w',80.9,'2019-4-8');"

cur.execute(sql) # 执行语句

db.commit() # 将写操作提交,多次写操作可一块提交

# 关闭数据库
cur.close()
db.close()

