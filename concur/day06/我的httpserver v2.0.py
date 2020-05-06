"""
httpserver v 2.0
"""

from socket import *
from select import *

# 具体功能实现
class HTTPServer:
    def __init__(self,host='0.0.0.0',port=8000,dir=None):
        self.host = host
        self.port =  port
        self.dir = dir
        self.addr = (host,port)
        # 实例化时直接创建套接字
        self.create_socket()
        self.bind()
        self.rlist = []
        self.wlist = []
        self.xlist = []

    # 创建套接字
    def create_socket(self):
        self.sockfd = socket() # create a new attribute
        self.sockfd.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)

    # 绑定地址
    def bind(self):
        self.sockfd.bind(self.addr)

    # 启动服务
    def serve_forever(self):
        self.sockfd.listen(3)
        print("Listen the port %d"%self.port)
        self.rlist.append(self.sockfd)

        while True:
            rs,ws,xs = select(self.rlist,self.wlist,self.xlist)
            for r in rs:
                if r is self.sockfd:
                    c, addr = r.accept()  # 考虑c是否可以变成self.c,handle中使用c时,
                                        # 这里如果有新的链接产生,self.c会覆盖前一个self.c
                    print("Connect from", addr)
                    self.rlist.append(c)
                else:
                    self.handle(r) # 处理客户端具体请求
    def handle(self,connfd):
        # 接收HTTP请求
        request = connfd.recv(1024)
        # 客户端断开的时候处理
        if not request:
            self.rlist.remove(connfd)
            connfd.close()
            return
        # 提取请求内容(字节穿安航分割)
        requset_line = request.splitlines()[0] # 取第一行
        print(request)
        print(requset_line)
        info = requset_line.decode().split(' ')[1]  # 获取请求内容
        print(connfd.getpeername(),':',info)

        # 根据请求内容进行数据整理
        # 分为两类,1.请求网页 2.其他
        if info == '/' or info[-5:] == '.html':
            self.get_html(connfd,info)
        else:
            self.get_data(connfd, info)

    # 返回网页
    def get_html(self,connfd,info):
        if info == '/':
            # 请求主页
            filename = self.dir + "/index.html"
        else:
            filename = self.dir +info
        try:
            fd = open(filename)
        except Exception:
            # 网页不存在
            response = "HTTP/1.1 404 NOT Found\r\n"
            response += 'Content-Type:text/html\r\n'
            response += '\r\n'
            response += '<h1>Sorry....</h1>'
        else:
            response = "HTTP/1.1 200 OK\r\n"
            response += 'Content-Type:text/html\r\n'
            response += '\r\n'
            response += fd.read()
        finally:
            connfd.send(response.encode())

        # f_name = requset_line.decode().split(' ')[1].split('/')[1]
        # with open('f_name.html') as f:
        #     response = "HTTP/1.1 200 OK\r\n"
        #     response += "Content-Type:text/html\r\n"
        #     response += "\r\n"
        #     response += f.read()
        # connfd.send(response.encode())

        # 其他数据
    def get_data(self,connfd, info):
        response = "HTTP/1.1 200 OK\r\n"
        response += 'Content-Type:text/html\r\n'
        response += '\r\n'
        response += "<h1>Waiting for httpserver 3.0</h1>"
        connfd.send(response.encode())



# 用户使用HTTPServer
if __name__ == "__main__":
    """
        通过HTTPServer类快速搭建服务,展示自己的网页
    """
    HOST = '0.0.0.0'
    PORT = 8000
    DIR = './static' # 网页存储位置
    httpd = HTTPServer(HOST,PORT,DIR) # 实例化对象
    httpd.serve_forever() #启动服务