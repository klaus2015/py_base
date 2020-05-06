"""
fork.py fork进程创建演示1.
 父进程先运行完,子进程(sleep(1))运行可能会丢失终端导致打印不出来,终端上不会丢失

 父子进程谁退出不会影响对面的继续运行
"""
import os
from time import sleep

# 创建子进程
pid = os.fork()

if pid < 0:
    print("Create process failed")
# 子进程执行部分
elif pid == 0:
    sleep(3)
    print("The new process")
# 父进程执行部分
else:
    sleep(4) # 父子进程运行总共耗时4s
    print("The old process")
# 父子进程都会执行
print("Fork test over")