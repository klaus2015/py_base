from socket import *
from multiprocessing import Process
import os
import signal

HOST = '0.0.0.0'
PORT = 8888
ADDR = (HOST,PORT)


s = socket()
s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
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
    p = Process(target=handle,args=(c,))
    p.daemon = True # 父进程(服务器退出),子进程终止,即停止所有服务
    p.start()
    # p.join() 不能加join,上面有signal处理僵尸进程,还有这里加join会阻塞程序,运行完这个子进程主进程才会接收下一个客户端
