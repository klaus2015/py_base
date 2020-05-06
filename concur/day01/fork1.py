"""
fork.py fork进程创建演示2
"""

import os
from time import sleep

print("===========================") # 子进程会复制父进程全部内存空间,从fork下一句开始执行。,不执行这里
a = 1

# 创建子进程
pid = os.fork() #  子进程从fork下一句开始执行

if pid < 0:
    print("Create process failed")
elif pid == 0:
    print("The new process")
    print("a = ",a) # 从父进程继承空间a
    a = 10000 # 修改自己的a
else:
    sleep(1)
    print("The old process")
    print("a:",a)

print("All a->",a) # 父子进程都执行