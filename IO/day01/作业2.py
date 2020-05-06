"""
      3. 编写一个程序，向一个文件中写入如下内容：
     　　　
     　　1.  2019-1-1  18:18:18
     　　2.  2019-1-1  18:18:19
     　　3.  2019-1-1  18:18:24

        循环每隔１秒写入一次,序号从１排列
        ctrl-c结束程序，下次启动程序
        序号要与之前的衔接

"""
# f = open("work.txt","rb")
# while True:
#     f.write()
import time
f = open('log.txt','a+')
f.seek(0,0)
n = 0
for line in f:
    n += 1
while True:
    n += 1
    time.sleep(1)
    s = "%d. %s\n"%(n,time.ctime())
    f.write(s)
    f.flush()


