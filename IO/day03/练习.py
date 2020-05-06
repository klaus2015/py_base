"""
http响应测试
"""
from socket import *
s = socket(AF_INET,SOCK_STREAM)
s.bind(('0.0.0.0',8000))
s.listen(5)

# while True:
#     c,addr = s.accept()
c,addr = s.accept()
print("Connect from",addr)
data = c.recv(4096) # 接收ｈｔｔｐ请求
print(data)