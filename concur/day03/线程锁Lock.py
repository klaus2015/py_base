"""
thread_lock线程锁
"""

from threading import Thread,Lock

lock = Lock() # 定义锁
a = b = 0

def value():
    while True:
        lock.acquire() # 上锁
        if a != b:
            print("a=%d,b=%d"%(a,b))
        lock.release() # 解锁

t = Thread(target=value)

t.start()
while True:
    with lock:  # 上锁
        a += 1
        b += 1
                # 执行完22 23 解锁 with代码块结束自动解锁 ,这样a一直等于b
t.join()