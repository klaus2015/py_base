from socket import *
from multiprocessing import Process
import signal,sys
from 我的dict.mysql import Database

# 全局变量
HOST = '0.0.0.0'
PORT = 8000
ADDR = (HOST,PORT)
# 建立数据库对象
db = Database(database='dict')

# 注册处理
def do_register(c,data):
    tem = data.split(' ')
    name = tem[1]
    psw = tem[2]
    # 返回True 注册成功 False 失败
    if db.register(name,psw):
        c.send(b'OK')
    else:
        c.send(b'Fail')
# 登录
def do_login(c,data):
    tem = data.split(' ')
    name = tem[1]
    psw = tem[2]
    if db.login(name,psw):
        c.send(b'OK')
    else:
        c.send(b'Fail')
# 查单词
def do_query(c,data):
    tem = data.split(' ')
    name = tem[1]
    word = tem[2]

    # 插入单词
    db.insert_hist(name, word)

    # 没找到返回None --找到返回单词解释
    mean = db.query(word)
    if not mean:
        c.send("没有找到该单词".encode())
    else:
        msg = "%s : %s"%(word,mean)
        c.send(msg.encode())
# 查历史记录
# def do_history(c,data):
#     name = data.split(' ')[1]
#     re = db.do_history(name)
#     for w in re:
#         c.send(w[0].encode())
#         sleep(0.01)
#     c.send('##'.encode())

# def do_history(c,data):
#     tem = data.split(' ')
#     name = tem[1]



# 具体处理客户端请求
def request(c):
    db.create_cursor() # 每个子进程单独生成游标
    # 循环接收请求
    while True:
        data = c.recv(1024).decode()
        print(data)
        if not data or data[0] == 'E':
            sys.exit() # 对应子进程退出
        elif data[0] == 'R':
            do_register(c,data)
        elif data[0] == 'L':
            do_login(c,data)
        elif data[0] == 'Q':
            do_query(c,data)
        elif data[0] == 'H':
            do_history(c,data)


def main():
    s = socket()
    s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
    s.bind(ADDR)
    s.listen(5)
    signal.signal(signal.SIGCHLD,signal.SIG_IGN)
    print("Listen the port 8000")
    while True:
        try:
            c,addr = s.accept()
            print("Connect from",addr)
        except KeyboardInterrupt:
            s.close()
            db.close()  # --其实就是db.db.close() 也可以自己写一个函数,调用它关闭数据库模块里的db关闭
            sys.exit("服务器退出")
        except Exception as e:
            print("Error:",e)
            continue
        # 给客户端创建子进程
        p = Process(target=request,args=(c,))
        p.daemon = True
        p.start()

main() # 启动程序


