


from threading import Thread
from time import sleep


def fun():
    sleep(3)
    print("线程属性测试")

t = Thread(target=fun)
t.start()
print(t.getName()) # Thread-1

print("哈哈")  # 主线程运行完不影响分之线程的继续运行