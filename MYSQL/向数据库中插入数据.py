import pymysql,re

db = pymysql.connect(host='localhost',
                     port=3306,
                     user='root',
                     password='123456',
                     database='country',
                     charset='utf8')

cur = db.cursor()
data_list = []
for i in range(2000000):
    name = 'tom_%s'%(i)
    data_list.append(name)
print(data_list)

sql = "insert into students(name) values(%s);"
cur.executemany(sql,data_list)
db.commit()

# 关闭数据库
cur.close()
db.close()
