"""
    测试用例
        进程,多进程,多线程
"""
from multiprocessing import Process
from threading import Thread
import time

# 计算  一个进程计算10次
def count(x,y):
    c = 0
    while c < 7000000:
        x += 1
        y += 1
        c += 1

# 单进程运行十遍
# t = time.time()
# for i in range(10):
#     count(0,0)
# print("%.3f"%(time.time()-t)) # 7.738


# 10个进程计算

# jobs = []
#
# for i in range(10):
#     p = Process(target=count,args=(0,0))
#     p.start()
#     t1 = time.time()
#     jobs.append(p)
# for i in jobs:
#     i.join()
# t2 = time.time()
# print(t2-t1)  # 3.138

# 创建多个线程
jobs =[]

for i in range(10):
    t = Thread(target=count,args=(0,0))
    jobs.append(t)
    t1 = time.time()
    t.start()

for i in jobs:
    i.join()
t2 = time.time()
print(t2-t1) # 6.691
