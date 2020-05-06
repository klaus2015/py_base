"""
udp_client.py  udp客户端流程
重点代码
# udp服务端和客户端先运行谁都可以
"""

from socket import *

#　服务器地址
ADDR = ('127.0.0.1',8888)

#　创建套接字
sockfd = socket(AF_INET,SOCK_DGRAM)

#　循环收发消息
while True:
    data = input("Msg>>")
    if not data:  # 客户端输入空退出客户端,服务端不需要任何处理,因为本身udp客户端和服务端就是无连接的
        break
    sockfd.sendto(data.encode(),ADDR)
    msg,addr = sockfd.recvfrom(1024)
    print("From server:",msg.decode())

sockfd.close()

# udp也有发送缓冲区,但是不会产生粘包问题,
# 流式套接字比喻成一个管子,两个人在放水,
# 数据包传输是把水冻成冰块---即有边界,所以一定不会产生粘包 ---
# 来不及接收的数据就会丢失,对于udp无连接来说,根本不知道每一次给我发送的客户端是谁,
# 所以无法区分连续给我发消息的是一个客户端,还是两个客户端,
