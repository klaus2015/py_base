"""
poll_server 完成TCP并发服务
重点代码
思路分析:
    IO多路复用实现并发
    建立fileno--->IO对象字典用于IO查找
"""
from socket import *
from select import *

# 创建监听套接字,作为关注的IO
s = socket()
s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
s.bind(("0.0.0.0", 8888))
s.listen(3)

# 创建poll对象
p = poll()

# 建立查找字典,通过一个IO的fileno找到IO
# 始终和register的IO保持一致
fdmap = {s.fileno(): s}

# 关注s
p.register(s, POLLERR | POLLIN)   # event 要关注的IO事件类型 不写的话,表示s的所有事态类型

# 循环监控IO发生
while True: # 大循环控制整个部分,里面有小循环就会一直阻塞在里面,无法产生新的链接
    events = p.poll()  # 阻塞等待监控的IO事件发生
    # 循环遍历列表,查看哪个IO就绪,进行处理
    for fd, event in events:  # fd,event = (3,1) 1代表
        print(events)
        # 区分哪个IO就绪
        if fd == s.fileno():
            c, addr = fdmap[fd].accept()
            print('Connect from', addr)
            # 关注客户端链接套接字
            p.register(c, POLLIN | POLLERR) # c关注了POLLIN和POLLERR
            fdmap[c.fileno()] = c  # 维护字典
        elif event & POLLIN:  # 按位与 判断是否是POLLIN就绪,如是才执行下面代码
            data = fdmap[fd].recv(1024).decode()
            if not data:
                p.unregister(fd)  # 取消关注 IO对象或者IO对象的fileno
                fdmap[fd].close()  # 关闭链接套接字
                del fdmap[fd]  # 从字典删除
                continue
            print(data)
            fdmap[fd].send(b'OK')

# In [11]: select.POLLIN    # & 按位与 判定属性是否存在
# Out[11]: 1                # | 按位或 增加一个属性
#
# In [12]: select.POLLERR
# Out[12]: 8
#
# In [13]: select.POLLOUT
# Out[13]: 4
