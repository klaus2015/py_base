"""
fork_sever

"""
from socket import *
import os
import signal # 父进程不退出,子进程变成僵尸进程

# 全局变量
HOST = '0.0.0.0'
PORT = 8888
ADDR = (HOST,PORT)

# 创建监听套接字
s = socket()
s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1) # 端口重用
s.bind(ADDR)
s.listen(5)

# 处理僵尸进程
signal.signal(signal.SIGCHLD,signal.SIG_IGN)
print("Listen the port 8888...")

# 具体处理客户端请求
def handle(c):
    while True:
        data = c.recv(1024)
        if not data:
            break
        print(data.decode())
        c.send(b'OK')
    c.close()




while True:
    # 循环处理客户端链接
    try:
        c,addr = s.accept()
        print("Connect from",addr)
    except KeyboardInterrupt:
        os.exit(0)
    except Exception as e:
        print(e)
        continue
    # 创建子进程处理客户端事物
    pid = os.fork()
    if pid == 0:
        s.close()  # 子进程中s无用
        handle(c)  # 处理具体食物
        os._exit(0) # 子进程销毁
    else:
        c.close() # 父进程不需要和子进程通信,父进程的作用是来链接客户端请求的