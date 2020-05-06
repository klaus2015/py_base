"""
    Thread
        线程函数参数传递
        同时创建多个线程
        主线程不执行任务,任务都交给分支线程去完成
"""
from threading import Thread
from time import sleep


# 含有参数的线程函数
def fun(sec,name):
    print("线程函数参数")
    sleep(sec)
    print("%s执行完毕"%name) # 打印结果无序,从sleep()中出来顺序不一定


jobs =[]

# 创建多个线程
for i in range(5):  # 循环创建五个线程
    t = Thread(target=fun,args=(2,),
               kwargs={"name":'T%d'%i})
    jobs.append(t)  # 存储线程对象
    t.start()

for i in jobs:
    i.join()