
from socket import *
import struct
st = struct.Struct('i32sif')

#　服务器地址
ADDR = ('127.0.0.1',8888)

#　创建套接字
sockfd = socket(AF_INET,SOCK_DGRAM)

#　循环收发消息
while True:
    print("+++++++++++++++++++++++++++++++++++++++")
    name = input("Name:").encode()
    age = int(input("age:"))
    id = int(input("id:"))
    score = int(input("score:"))
    data = st.pack(id,name,age,score)  # pack返回值是字节串

    sockfd.sendto(data,ADDR)



sockfd.close()