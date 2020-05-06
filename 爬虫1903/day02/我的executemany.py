import pymysql

# db = pymysql.connect('localhost','root','123456','maoyan',charset='utf8')
db = pymysql.connect('localhost','root','123456','maoyan',charset='utf8')

cursor = db.cursor()

ins = 'insert into filmtab values(%s,%s,%s)'

f = (['zxm','zxm','2019-10-18'],['cx','cx','2018-7-12'])
cursor.executemany(ins,f)
db.commit()
cursor.close()
db.close()