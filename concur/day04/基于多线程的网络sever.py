"""
thread_sever------基于threading的多线程并发

"""

from threading import Thread
from socket import *
import sys

def handle(c):
    while True:
        data = c.recv(1024)
        if not data:
            break
        print(data.decode())
        c.send(b'OK')
    c.close()
# 全局变量
HOST = '0.0.0.0'
PORT = 8888
ADDR = (HOST,PORT)
# 创建套接字,监听
s = socket()
s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1) # 端口重用
s.bind(ADDR)
s.listen(5)
# 线程不用signal清理,--不会产生僵尸
print("Listen the port 8888....")

# 循环等待链接
while True:
    try:
        c,addr = s.accept()
        print("Connect from",addr)
    except KeyboardInterrupt:
        sys.exit('退出服务器')
    except Exception as e:
        print(e)
        continue
    # 创建线程处理请求
    t = Thread(target=handle,args=(c,))
    t.setDaemon(True) # 主线程提出,所有分支线程都退出
    t.start()
