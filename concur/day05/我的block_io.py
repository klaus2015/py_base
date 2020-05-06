"""
block_io
socket 非阻塞io
"""
from socket import *
import time

# 打开日志文件
f = open('log.txt','a+')

# ctp套接字
sockfd = socket()
sockfd.bind(('127.0.0.1',8888))
sockfd.listen(3)

# 设置套接字为非阻塞
# sockfd.setblocking(False)

# 设置超时检测  不会和非阻塞一起使用
sockfd.settimeout(3)  # 阻塞三秒 # accept()阻塞等待三秒,然后执行f.write,
                        # 不会让accept()一直阻塞在,然后再回过来检测accept()是否准备好

while True:
    print("Waiting for connenct...")
    # 没有客户端链接,每隔三秒写一条日志
    try:
        connfd,addr = sockfd.accept()
    except (BlockingIOError,timeout) as e:  # 可以捕获多种异常
        time.sleep(3)
        f.write("%s : %s\n"%(time.ctime(),e))
        f.flush()
    else:
        print("Connect from",addr)
        data = connfd.recv(1024).decode()
        print(data)
