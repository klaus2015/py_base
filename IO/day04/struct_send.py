'''
使用ｕｄｐ完成, 客户端不断录入学生信息
将其发送到服务端，在服务端，将学生信息写入到
一个文件中，每个学生信息占一行
'''

from socket import *
import struct

# 数据格式定义
st = struct.Struct('i32sif') # 32表示字符串的长度一个汉字占三个字节

# udp套接字
s = socket(AF_INET,SOCK_DGRAM)
ADDR = ('127.0.0.1',8888)

while True:
    print("============================")
    id = int(input("ID:"))
    name = input('Name:').encode() # 如果名字长度超过32字节,多余的在接收方被转换回来后会丢失,如果短于32(一般都会短),转换回来后面会加0补够
    age = int(input("Age:"))
    score = float(input('Score:')) # 浮点型转换为二进制再转换回来,有可能会变成这个数的近似值,应为可能除2除不尽,又有一定的长度限制
    # 打包数据发送  可以和其他编程语言进行交互,---好处
    # 将一组简单的数据进行打包--包括字节串,整型和浮点型,转换成字节串格式发送,格式为C语言,网络收发的格式解析和打包的标准是C语言
    data = st.pack(id,name,age,score)
    s.sendto(data,ADDR)