"""
pymysql 读取操作--select
"""
import pymysql

#链接数据库
db = pymysql.connect(host='localhost',
                     port=3306,
                     user='root',
                     password='123456',
                     database='dict',
                     charset='utf8')

# 获取游标  (操作数据库,执行sql语句)
cur = db.cursor()


# 读取数据库数据

sql = "select word from hist where name= 'zxm';"
cur.execute(sql) # 执行正确后cur调用函数获取结果

# 获取一个查询结果
# one_row = cur.fetchone()
# print(one_row) # 元组 ---('a',)
#
# # 获取多个查询结果
many_row = cur.fetchmany(2) # 接着fetchone()查询的位置,继续向后查询
print(many_row)  # ---(('a',), ('a',))  元组套元组

# 获取所有查询结果
# all_row = cur.fetchall()
# print(all_row)













# 关闭数据库
cur.close()
db.close()