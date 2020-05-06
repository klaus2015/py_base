from multiprocessing import Process
from multiprocessing import Queue
from time import sleep
from random import randint


q = Queue(5)

def handle():
    for i in range(6):
        x = randint(1,33)
        q.put(x)
    q.put(randint(1,16)) # 消息队列满,put阻塞

def request():
    while True:
        # print("开始摇号")
        sleep(2)
        try:
            print(q.get([3])) # 消息队列空,get阻塞
        except:
            break
p1 = Process(target=handle)
p2 = Process(target=request)
p1.start()
p2.start()
p1.join()
p2.join()





