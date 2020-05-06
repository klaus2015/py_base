"""
httpserver v1.0
基本要求：1.获取来自浏览器的请求
　　　　　2.判断如果请求内容是/ 将index.html返回给客户端
　　　　　3.如果请求的是其他内容则返回404　
"""

from socket import *

#　客户端(浏览器)处理
def request(connfd):
    # 获取请求将请求内容提取出来
    data = connfd.recv(4096)
    if not data:
        return
    request_line = data.decode().split('\n')[0]
    info = request_line.split(' ')[1]

    # 判断是/ 则返回index.html 不是则返回404
    if info == '/':
        with open('index.html')as f:   # 请求行和空行必须要有,请求体和请求头可以没有
            response = "HTTP/1.1 200 ok\r\n"
            response += "Connext_Type:Text/html\r\n"
            response += '\r\n'
            response += f.read()


    else:
        return '404:not found'



#　搭建ｔｃｐ网络
sockfd = socket()
sockfd.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
sockfd.bind(('0.0.0.0',8000))
sockfd.listen(3)
while True:
    connfd,addr = sockfd.accept()
    data = request(connfd) #　处理客户端请求  ---这时客户端即浏览器返送过来的请求
    n = connfd.send(data)
    # connfd.close()
