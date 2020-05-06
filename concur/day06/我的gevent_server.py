"""
    基于协程的tcp并发
    思路:
        1.将每个客户端的处理设置为协程函数
        2.让socket模块下的阻塞可以触发协程跳转
"""


import gevent
from gevent import monkey
monkey.patch_all() # 执行脚本,修改socket阻塞
from socket import *


def handle(c):
    while True:
        data = c.recv(1024).decode()
        if not data:
            break
        print(data)
        c.send(b'OK')

s = socket()
s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
s.bind(('127.0.0.1',8888))
s.listen(5)

# 巡检接收客户端链接
while True:
    c,addr = s.accept()
    print("Connect from",addr)

    # handle(c) # 处理具体的客户端请求
    gevent.spawn(handle,c)