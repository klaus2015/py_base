"""
udp_server.py ｕｄｐ套接字服务端流程
重点代码
"""

from socket import *
import struct
st = struct.Struct('i32sif')

#　创建套接字
sockfd = socket(AF_INET,SOCK_DGRAM)

#　绑定地址
server_addr = ('127.0.0.1',8888)
sockfd.bind(server_addr)


# 打开文件
f = open('student.txt','a')

# 循环收发消息
while True:
    data,addr = sockfd.recvfrom(1024)   # 接受到的是元组(1,b'lily',14,92.5)
    data = st.unpack(data)

    info= "%d   %-10s   %d   %.1f\n"%data
    f.write(info)
    f.close()



#　关闭套接字
sockfd.close()