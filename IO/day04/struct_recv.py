'''
使用ｕｄｐ完成, 客户端不断录入学生信息
将其发送到服务端，在服务端，将学生信息写入到
一个文件中，每个学生信息占一行
'''

from socket import *
import struct

# 和客户端一致 如果不一样会报错
st = struct.Struct('i32sif')

# udp套接字
s = socket(AF_INET,SOCK_DGRAM)
s.bind(('127.0.0.1',8888))

# 打开文件
f = open('student.txt','a')

while True:
    data,addr = s.recvfrom(1024)
    # (1,b'Lily',14,92.5)
    data = st.unpack(data)

    # 写入文件
    info = "%d   %-10s  %d  %.1f\n"%data
    f.write(info)
    f.flush()




