"""
    线程基础使用
        线程是挖取进程的一部分,进程是从新开辟一块空间,注意区别
        线程空间的测试

"""


from threading import Thread
from time import sleep
import os

a = 1
#线程函数
def music():
    for i in range(3):
        sleep(2)
        print(os.getpid(),"播放:夜上海")
    global a
    print("a=",a)   # a= 1
    a = 1000

t = Thread(target=music)
t.start()
for i in range(4):
    sleep(1)
    print(os.getpid(),"播放:葫芦娃")
t.join()
print("a:",a)   # 1000    线程是挖取进程的一部分,进程是从新开辟一块空间,注意区别