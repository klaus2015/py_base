"""
ftp 文件服务,客户端
"""
from socket import *
import sys,time

ADDR = ('127.0.0.1',8080)

# 客户端文件处理类
class FTPClient:
    """
    客户端处理 查看 上传下载 退出
    """
    def __init__(self,sockfd):
        self.sockfd = sockfd
    def do_list(self):
        self.sockfd.send(b'L') # 发送请求,在服务器根据不同请求再分类处理
        # 等待回复
        data = self.sockfd.recv(128).decode()
        if data == 'OK':
            # 一次接收文字字符串
            data = self.sockfd.recv(4096)
            print(data.decode()) # 服务器用换行拼接文件名,这里直接打印
    # 下载文件
    def do_get(self,filename):
        self.sockfd.send(b'G ' + filename.encode())
        data = self.sockfd.recv(128).decode()
        if data == 'OK':
            f = open(filename,'wb')
            # 循环接收写入文件
            while True:
                data = self.sockfd.recv(1024)
                if data == b'##': # 发送这个标志代表传输完成  # 网络传输中不能发送"空"
                    break
                f.write(data)
            f.close()
        else:
            print(data)
    # def do_put(self,filename):  # 1,一切的前提是在文件存在的基础上.2,需要考虑传入带路径的文件的可能性
    #     self.sockfd.send(b'P ' + filename.encode())
    #     data = self.sockfd.recv(128).decode()
    #     if data == 'OK':
    #         f = open(filename,'rb')
    #         # 循环读取文件
    #         while True:
    #             data = f.read(1024)  # data 以rb读取,不用encode()
    #             if not data:
    #                 time.sleep(0.1)
    #                 self.sockfd.send(b'**')
    #                 break
    #             self.sockfd.send(data)
    #         f.close()
    #     else:
    #         print(data)

    def do_out(self,filename):  # 老师的思路
        try:
            f = open(filename,'rb')
        except FileNotFoundError:
            print("文件不存在")
            return
        filename = filename.split('/')[-1]
        self.sockfd.send(b'P ' + filename.encode())
        data = self.sockfd.recv(128).decode()
        if data == 'OK':
            while True:
                data = f.read(1024)
                if not data:
                    time.sleep(0.1)
                    self.sockfd.send(b'##')
                    break
                self.sockfd.send(data)
            f.close()
        else:
            print(data)
    def do_quit(self):
        self.sockfd.send(b'Q')# 请求退出
        self.sockfd.close() # 客户端就一个任务,此任务结束,表示客户端也退出了
        sys.exit("谢谢使用")




# 创建套接字
def main():
    s = socket()
    try: # 一切功能建立在链接上的基础上,所以加try
        s.connect(ADDR)
    except Exception as e:
        print(e)
        return
    # 实例化对象,调用文件处理方法
    ftp = FTPClient(s)  # 将套接字变成类的属性,方便其他方法使用
    while True:
        print("\n=======命令选项=========")
        print("******   list    *********")
        print("******   get file    *********")
        print("******   put file   *********")
        print("******   quit    *********")
        print("\n=======命令选项=========")

        cmd = input("请输入命令: ")
        if cmd.strip() == 'list': # 根据功能想参数
            ftp.do_list()
        elif cmd[:3].strip() == 'get': # 前三个字母是get
            filename = cmd.strip().split(' ')[-1]  # [1]没有[-1]好,防止get后面加了两个空格
            ftp.do_get(filename)
        elif cmd[:3].strip() == 'put':
            filename = cmd.strip().split(' ')[-1]
            ftp.do_put(filename)
        elif cmd.strip() == 'quit':
            ftp.do_quit()
        else:
            print("请输入正确命令")


if __name__ == "__main__":
    main()