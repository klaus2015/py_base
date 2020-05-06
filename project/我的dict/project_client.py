"""
dict 客户端
功能:根据用户输入发送请求,得到结果
    一级: 注册 登录 退出
    二级: 查单词 历史记录 注销
"""
from socket import *
import sys
from getpass import getpass

ADDR = ('127.0.0.1',8000)
s = socket()   # 大多数函数都需要套接字作为参数,所有设为全局变量
s.connect(ADDR)

# 注册
def do_register():
    while True:
        name = input("姓名: ") # 用户名是不能包含空格,所以服务器可以按空格切割
        psw = getpass()  # 细节
        psw1 = getpass("Again:") # 细节
        if psw != psw1:  # 密码输两次,验证是否一样--细节
            print("两次密码不一致")
            continue
        if " " in name or ' ' in psw:# ---细节
            print("密码不能有空格")
            continue
        msg = "R %s %s"%(name,psw) # ---细节  --先建立字符串
        s.send(msg.encode())
        data = s.recv(128).decode()
        if data == 'OK':
            print("注册成功")
            login(name)
        else:
            print("注册失败")
        return

# 登录
def do_login():
    # while True:
    name = input("姓名: ")
    psw = getpass()
    msg = "L %s %s"%(name,psw)
    s.send(msg.encode())
    data = s.recv(128).decode()
    if data == 'OK':
        print("登录成功")
        login(name)
    else:
        print("登录失败")

# 查单词
def do_query(name):
    while True:
        word = input("请输入单词: ")
        if word == '##': # 输入##结束查询
            break
        else:
            msg = "Q %s %s"%(name,word)
            s.send(msg.encode()) # 发送请求
            # 得到查询结果
            data = s.recv(2048).decode()
            print(data)
# 查历史记录
def do_history(name):
    msg = "H %s"%name
    s.send(msg.encode())
    while True: # 不知道记录有多少条,就用死循环,待接收到特定符号后结束
        data = s.recv(128).decode()
        if data == '##':
            break
        print(data)

# def do_history(name):
#     msg = "H " + name
#     s.send(msg.encode())
#     data = s.recv(128)
#     if data == 'OK':
#         while True:
#             data = s.recv(128)
#             if data == '##':
#                 break
#             print(data.decode())


def login(name):
    while True:
        print("""
        =========Query===========
        1.查单词    2.历史记录    3.注销
        ===========================
        """)
        cmd = input("输入选项: ")
        if cmd == '1':
            do_query(name)
        elif cmd == '2':
            do_history(name)
        elif cmd == '3':
            break
            # return # 也可以
        else:
            print("请输入正确选项")

def main(): # 启动函数 基本网络搭建好后运行客户端和终端,同时链接服务器测试网络连接和多进程
    while True:
        print("""
        =========Welcome===========
        1.注册    2.登录    3.退出
        ===========================
        """)
        cmd = input("输入选项: ")
        if cmd == '1':
            do_register()
        elif cmd == '2':
            do_login()
        elif cmd == '3':
            s.send(b'E')
            sys.exit("谢谢使用")
        else:
            print("请输入正确选项")



main()