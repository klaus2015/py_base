"""
    线程基础使用
        基本同Process
        1.封装线程函数
        2.创建线程对象
        3.启动线程
        4.回收线程

"""


from threading import Thread
from time import sleep
import os

#线程函数
def music():
    for i in range(3):
        sleep(2)
        print(os.getpid(),"播放:夜上海")

t = Thread(target=music)
t.start()
for i in range(4):      # 17 和24 在同一个线程中,即主线程中
    sleep(1)
    print(os.getpid(),"播放:葫芦娃")
t.join()
# print("haha")
