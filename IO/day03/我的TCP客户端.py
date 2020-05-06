from socket import *

sockfd = socket()

# 连接服务器
sockfd.connect(('127.0.0.1',20190))

# 发送消息
while True:
    data = input("Msg>>")
    # if data == "":    # 发""没有意义
    #     break
    if not data:
        break
    sockfd.send(data.encode())

    data = sockfd.recv(1024)
    print("Server",data.decode())

sockfd.close()

