from socket import *

ADDR = ('0.0.0.0',20190)
s = socket()
s.bind(ADDR)
s.listen(5)
while True:
    print("Waiting for connect...")
    try:
        connfd,addr = s.accept()
        print("Connect from", addr)
    except KeyboardInterrupt:
        print("Server exit")
        break
    except Exception as e:
        print(e)
        continue


    while True:
        data = connfd.recv(1024)
        if not data:
            break
        print("收到:", data.decode())
        n = connfd.send(b'Thanks')
        print("发送了%d个字节"%n)

    connfd.close()
s.close()


