from multiprocessing import Process
from threading import Thread
import time
# IO
def io():
    write()
    read()

def write():
    f = open('test','w')
    for i in range(1800000):
        f.write("Hello world\n")
    f.close()

def read():
    f = open('test')
    lines = f.readlines()
    f.close()

# 单进程执行十遍

# t = time.time()
# for i in range(10):
#     io()
# print("%.3f"%(time.time()-t))  # 3.894

# 多进程执行
# jobs = []
# for i in range(10):
#     p = Process(target=io)
#     jobs.append(p)
#     t = time.time()
#     p.start()
#     print(p.pid)
# for i in jobs:
#     i.join()
# t1 = time.time()
# print("%.3f"%(t1-t))  # 2.020

# 多个线程
jobs = []
for i in range(10):
    t = Thread(target=io)
    jobs.append(t)
    t1 = time.time()
    t.start()
for i in jobs:
    i.join()
    t2 = time.time()
print("%.3f"%(t2-t1))  # 6.344

