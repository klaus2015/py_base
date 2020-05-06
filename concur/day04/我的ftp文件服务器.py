# tcp套接字   考虑粘包问题
# 多线程
# 服务器文件夹以什么类型存储

from socket import *
from threading import Thread
import sys,os,time

# 服务器地址
ADDR = ('0.0.0.0',8080)
FTP = "/home/tarena/FTP/" # 文件库 FTP后加/方便后面拼接文件

# 创建类实现服务器文件处理功能
class FTPServer(Thread):
    """
        查看列表,下载,上传,退出处理
    """
    def __init__(self,connfd):
        self.connfd = connfd
        super().__init__()
    def do_list(self):
        """
            获取文件列表
        :return:
        """
        files = os.listdir(FTP)
        if not files:
            self.connfd.send("文件库空".encode())
        else:
            self.connfd.send(b'OK') # 发完OK,后面就需要发送文件列表,防止粘包,所以下面需要阻塞一下
            time.sleep(0.1)
        filelist = ""
        for file in files:
            if file[0] != '.' and os.path.isfile(FTP+file): # 判断是隐藏文件和文件夹不发送
                filelist += file + '\n'
        self.connfd.send(filelist.encode())
    def do_get(self,filename): # 存在OK,不存在回复不存在
        try:
            f = open(FTP+filename,'rb')
        except Exception:
            # 打开文件失败
            self.connfd.send('文件不存在'.encode())
            return
        else:
            self.connfd.send(b'OK')
            time.sleep(0.1)
        # 发送文件
        while True:
            data = f.read(1024)
            if not data:
                time.sleep(0.1)
                self.connfd.send(b'##')
                break
            self.connfd.send(data)
    # 上传文件
    def do_put(self,filename):
        # files = os.listdir(FTP)   # 判断文件是否存在,我的思路,复杂
        # if filename in files:
        #     self.connfd.send("文件已存在".encode())
        #     return # 文件存在就结束本次上传
        if os.path.exists(FTP+filename):  # 老师的思路
            self.connfd.send("文件已存在".encode())
            return # 文件存在就结束本次上传
        else:
            self.connfd.send(b'OK')
            # time.sleep(0.1)   # 这边发送完OK,客户端就开始上传文件,此处不需要阻塞0.1s,
                                # 客户端上传完成后会阻塞0.1s,然后发送b'**'
            f = open(FTP+filename,'wb')
            while True:
                data = self.connfd.recv(1024)
                if data == b'**':
                    break
                f.write(data)
            f.close()






    # 循环接收请求,分情况调用功能函数
    def run(self):
        while True:
            data = self.connfd.recv(1024).decode()
            if not data or data == "Q": # not data 表示空,即客户端用CTRL+C退出
                return # 结束run 表示退出运行这个客户端的线程
            elif data == "L":
                self.do_list()
            elif data[0] == 'G':
                filename = data.split(' ')[-1]
                self.do_get(filename)
            elif data[0] == 'P':
                filename = data.split(' ')[-1]
                self.do_put(filename)




# 搭建网络 多线程并发模型
def main():
    s = socket()
    s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    s.bind(ADDR)
    s.listen(5)
    while True:
        try:
            c,addr = s.accept()
        except KeyboardInterrupt:
            sys.exit('退出服务器')
        except Exception as e:
            print(e)
        # 自定义线程类
        client = FTPServer(c)
        client.setDaemon(True)  # 主线程提出,所有分支线程都退出
        client.start() # 运行run

main()

