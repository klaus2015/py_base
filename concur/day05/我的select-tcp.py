"""
select  tcp服务
    将关注的IO放入监控列表
    当IO就绪是会通过select返回
    遍历列表

"""
from socket import *
from select import select

# 创建监听套接字
s = socket()
s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
s.bind(("0.0.0.0",8888))
s.listen(3)

# 设置关注列表
rlist = [s] # s 用于等待处理链接
wlist = []
xlist = []

# 循环监控IO
while True:
    rs,ws,xs, = select(rlist,wlist,xlist)

    # 遍历返回值列表,处理就绪的IO
    for r in rs:
        if r is s:
            c,addr = r.accept()  # c是链接套接字,专门与相对应的客户端收发消息,s是监听套接字,处理客户端的请求链接
            print("Connect from",addr)
            rlist.append(c)  # 增加新的IO关注,
        # 有客户端发消息
        else:
            data = r.recv(1024).decode()
            # 有客户端退出
            if not data: # 客户端断开,服务端也会收到一个空,是revc返回的
                rlist.remove(r)  # 取消对客户端关注
                r.close()
                continue  # 结束本次任务,继续for 循环处理下个任务
            print(data)
            r.send(b'OK')
            # wlist.append(r) # 谁给我发消息,把谁加到'写'的列表中

    # for w in ws:
    #     w.send(b'OK')
    #     wlist.remove(w) # 发完消息 移除这个对象,等待下次
    #
    # for x in xs:
    #     pass
