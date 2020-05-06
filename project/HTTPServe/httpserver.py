"""
httpserver部分的主程序
获取http请求
解析http请求
将请求发送给WebFrame
从WebFrame接收反馈数据
将数据组织为Response格式发送给客户端
"""
"""
httpserver 双向通信1/----浏览器,2/----webframe
"""
from socket import *
import sys,re,json
from threading import Thread
from config import *


# 服务器地址
ADDR = (HOST,PORT)

# 和ｗｅｂｆｒａｍｅ通信的函数
def connect_frame(env):
    s = socket()
    try:
        s.connect((frame_ip,frame_port))
    except Exception as e:
        print(e)
        return
        # 将字典转换为json
    data = json.dumps(env)
    # 将解析后的请求发送给webframe
    s.send(data.encode())
    # 接收来自webframe数据
    data = s.recv(4096 * 100).decode()
    return json.loads(data)


# 将httpserver 基本功能封装为类
class HTTPServer:
    def __init__(self):
        self.address = ADDR
        self.create_socket() # 和浏览器交互
        # self.connect_scoket() # 和应用程序 - Webframe交互　－－弊端，只能有一个链接套接字和ｗｅｂｆｒａｍｅ链接
        self.bind()

    def create_socket(self):
        self.sockfd = socket()
        self.sockfd.setsockopt(SOL_SOCKET,SO_REUSEADDR,DEBUG)

    # # 创建和webframe交互的套接字----在类里面创建和ｗｅｂｆｒａｍｅ链接的套接字，只会有一个链接套接字，多个线程共用一个链接套接字，会造成阻塞，速度慢
    # def connect_scoket(self):
    #     self.connect_sockfd = socket()
    #     frame_addr = (frame_ip,frame_port)
    #     try:
    #         self.connect_sockfd.connect(frame_addr)
    #     except Exception as e:
    #         print(e)
    #         sys.exit()
    def bind(self):
        self.sockfd.bind(self.address)
        self.ip = self.address[0]
        self.port = self.address[1]

    # 启动服务
    def server_forever(self):
        self.sockfd.listen(5)
        print("Listen the port %d"%self.port)
        while True:
            connfd,addr = self.sockfd.accept() # connfd 不能改成self.connfd,如果改成self.connfd,会被后面创建的链接套接字覆盖,一个线程对其修改会影响其他线程
            print("Connect from",addr)
            client = Thread(target=self.handle,args=(connfd,))
            client.setDaemon(True)
            client.start()

    # 处理具体客户端请求任务
    def handle(self,connfd):
        requset = connfd.recv(4096).decode() # 客户端突然断开 request会是 空
        # print(requset)
        pattern = r'(?P<method>[A-Z]+)\s+(?P<info>/\S*)'
        try:
            env = re.match(pattern,requset).groupdict() # 返回捕获组 组名和内容组成的字典
        except:
            # 客户端断开
            connfd.close()
            return
        else:
            data = connect_frame(env)
            # data = json.dumps(env) # 将字典转换为json
            # self.connect_sockfd.send(data.encode()) # 将解析后的请求发送给webframe
            #  #　接受来自ｗｅｂｆｒａｍｅ的数据
            # data = self.connect_sockfd.recv(4096*100).decode()
            self.response(connfd,data)

    #　给浏览器发送数据
    def response(self,connfd,data):
        # data = {'status': 200, 'data': 'xxxxxx'}--根据ｓｔａｔｕｓ确定响应情况
        if data['status'] == '200':
            responseHeaders = "HTTP/1.1 200 OK\r\n"
            responseHeaders += "Content-Type:text/html\r\n"
            responseHeaders += '\r\n'
            responseBody = data['data']
        elif data['status'] == '404':
            responseHeaders = "HTTP/1.1 404 OK\r\n"
            responseHeaders += "Content-Type:text/html\r\n"
            responseHeaders += '\r\n'
            responseBody = data['data']
        elif data['status'] == '500':
            pass
            # 给浏览器发送数据
        response_data = responseHeaders + responseBody
        connfd.send(response_data.encode())





httpd = HTTPServer() # 实例化对象的时候自动创建套接字
httpd.server_forever()