from multiprocessing import Semaphore,Process
from time import sleep
import os

sm = Semaphore(3) # (创建信号量)最大允许三个任务同时执行

def handle():
    sm.acquire()  # 想执行任务必须消耗一个信号量
    print("%s 执行任务"%os.getpid())
    sleep(2)
    print("%s 执行任务完毕"%os.getpid())
    sm.release() # 归还信号量
    print(sm.get_value())

for i in range(10):
    p = Process(target=handle)
    p.start()