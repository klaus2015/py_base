from socket import *
import os,sys

# 服务器地址
ADDR = ('176.23.4.107',9520)

# 发送消息
def send_msg(s,name):
    while True:
        try:
            text = input("发言:")
        except KeyboardInterrupt:
            text = "quit"
        # 输入quit退出
        if text.strip() == 'quit':
            msg = "Q " + name
            s.sendto(msg.encode(),ADDR)
            sys.exit("退出聊天室")
        msg = "C %s %s"%(name,text)
        s.sendto(msg.encode(),ADDR)

# 接收消息
def recv_msg(s):
    while True:
        try:
            data,addr = s.recvfrom(4096)
        except KeyboardInterrupt:
            sys.exit()
        # 从服务器收到EXIT退出
        if data.decode() == 'EXIT':
            sys.exit()
        print(data.decode())

#搭建网络
def main():
    s = socket(AF_INET,SOCK_DGRAM)

    #进入聊天室
    while True:
        name = input("姓名")          # 输入姓名可以是进入聊天室,也可能是发送消息,如何区别请求内容,分类,HTTP请求类别
        msg = "L " + name  # L后加空格,服务器好解析判断
        s.sendto(msg.encode(),ADDR)
        # 接收反馈
        data,addr = s.recvfrom(128)
        if data.decode() == "OK": # 协议,服务端返回OK代表可以进入
            print("您已进入聊天室")
            break
        else:
            print(data.decode())
    # 已经进入聊天室
    pid = os.fork()
    if pid < 0:
        sys.exit("Error")
    elif pid == 0:
        send_msg(s,name) # 子进程发送消息
    else:
        recv_msg(s) # 父进程负责接收消息

main()
