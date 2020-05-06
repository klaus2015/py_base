"""
进程对象属性
"""

from multiprocessing import Process
import time

def tm():
    for i in range(3):
        print(time.ctime())
        time.sleep(2)


p = Process(target = tm,name = 'tarena')

p.daemon = True # 父进程退出子进程也退出 ,必须在start前设置 ,如果不写这句,父进程执行完,不会影响子进程的执行

p.start()
time.sleep(7)
print("Name:",p.name) # 进程名称
print("PID：",p.pid) # 对应子进程PID
print("is alive:",p.is_alive()) # 是否在生命周期    这里执行完后,代表父进程结束,
                                # p.daemon = True,父进程结束,子进程也会结束,不需要再使用join()



