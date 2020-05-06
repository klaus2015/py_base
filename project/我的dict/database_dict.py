import pymysql,re


#链接数据库
db = pymysql.connect(host='localhost',
                     port=3306,
                     user='root',
                     password='123456',
                     database='dict',
                     charset='utf8')

# 获取游标  (操作数据库,执行sql语句)
cur = db.cursor()