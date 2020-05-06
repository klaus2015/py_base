"""
获取进程PID号
"""
import os
from time import sleep

pid = os.fork()
print("1",pid   )

if pid < 0:
    print("Error")
elif pid == 0:
    sleep(1)
    print("Child PID:",os.getpid()) # 子PID
    print("Get parent PID:",os.getppid()) #父PID
else:
    print("Get child PID:",pid) # 子PID
    print("Parent PID:",os.getpid()) #父PID
# 在终端中运行
# 1 4634
# Get child PID: 4634
# Parent PID: 4633
# 1 0
# tarena@tarena:~/1905/concur/day01$ Child PID: 4634
# Get parent PID: 2187 ---系统进程就会成为孤儿进程新的父进程,系统不重启,系统这个id一直固定
