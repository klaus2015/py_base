"""
words char
explain varchar()
"""

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
sql = "insert into words (word,expla) values(%s,%s)"
# try:
#     f = open('dict.txt','r')
#     for line in f:
#         # tem = line.split(' ')
#         # word = tem[0]
#         # expla = ' '.join(tem[1:]).strip()
#         # sql = "insert into words values(%s,%s)"
#         tup = re.findall(r'(\S+)\s+(.*)',line)[0]
#         cur.execute(sql,[word,expla])
#         db.commit()
f = open('dict.txt','r')
for line in f:
    tup = re.findall(r'(\S+)\s+(.*)', line)[0]
    try:
        cur.executemany(sql, tup)
        db.commit()

    except Exception as e:
        db.rollback()
        print(e)



# 关闭数据库
cur.close()
db.close()
