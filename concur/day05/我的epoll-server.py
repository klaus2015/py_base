"""
epoll_server 完成TCP并发服务
找
"""
from socket import *
from select import *

# 创建监听套接字,作为关注的IO
s = socket()
s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
s.bind(("0.0.0.0", 8888))
s.listen()

ep = epoll()

fdmap = {s.fileno(): s}

# 关注s
ep.register(s, EPOLLIN | EPOLLERR)

# 循环监控IO发生
while True:
    events = ep.poll()  # 阻塞等待监控的IO事件发生
    # 循环遍历列表,查看哪个IO就绪,进行处理
    for fd, event in events:
        # 区分哪个IO就绪
        if fd == s.fileno():
            c, addr = fdmap[fd].accept()
            print('Connect from', addr)
            # 关注客户端链接套接字
            p.register(c, EPOLLIN | EPOLLERR)
            fdmap[c.fileno()] = c  # 维护字典
        elif event & EPOLLIN:  # 按位与 判断是否是POLLIN就绪,如是才执行下面代码
            data = fdmap[fd].recv(1024).decode()
            if not data:
                p.unregister(fd)  # 取消关注
                fdmap[fd].close()  # 关闭链接套接字
                del fdmap[fd]  # 从字典删除
                continue
            print(data)
            fdmap[fd].send(b'OK')