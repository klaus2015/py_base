from socket import *
import os,sys

# 1所有或者大多数模块都会使用,或者2特殊含义的量,定义为全局变量
# 服务器地址
ADDR = ('0.0.0.0',8888) # 全局变量,大写,代表具有一定含义,不要再给他赋值
# 储存用户
user = {}

# 登录
def do_login(s,name,addr):
    if name in user or '管理员' in name:
        s.sendto("该用户已存在".encode(),addr)
        return
    s.sendto(b'OK',addr) # 可以进入聊天室  先通知其他人,再存储,防止将通知信息发给自己(自己看不到这个信息)
    # 通知其他人
    msg = "\n欢迎'%s'进入聊天室"%name
    for i in user:
        s.sendto(msg.encode(),user[i])
    user[name]=addr

# 聊天
def do_chat(s,name,text):
    msg = "%s: %s"%(name,text)
    for i in user:
        if i != name: # 刨除本人,其他都转发
            s.sendto(msg.encode(),user[i])
# 执行退出
def do_quit(s,name):
    msg = "\n%s退出聊天室"%name
    for i in user:
        if i != name: #其他人
            s.sendto(msg.encode(),user[i])
        else:
            s.sendto(b'EXIT',user[i])
    del user[name]
# 处理请求
def do_request(s):
    while True:
        data,addr = s.recvfrom(1024)
        tem = data.decode().split(" ") # 拆分请求
        # 根据不同的请求类型.执行不同内容
        if tem[0] == "L":
            do_login(s,tem[1],addr) # 执行具体工作
        elif tem[0] == "C":
            text = ' '.join(tem[2:])  # 字符串拼接
            do_chat(s,tem[1],text)
        elif tem[0] == "Q":
            do_quit(s,tem[1])



# 搭建网络
def main():
    s = socket(AF_INET,SOCK_DGRAM)
    s.bind(ADDR)
    pid = os.fork()
    if pid == 0:
        while True:
            # for i in user:  子进程中的user一直是空的
            #     s.sendto()
            msg = input("管理员消息: ")
            msg = "C 管理员 " + msg # 空格必须英文空格,中文空格split切不出来
            s.sendto(msg.encode(),ADDR)
    # 请求处理函数--功能/参数/返回值
    do_request(s)

main()