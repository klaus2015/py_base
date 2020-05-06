"""
模拟僵尸进程产生
现在系统比较智能,父进程退出,子进程也会被系统回收

# 服务器会出现如下问题
父进程不退出,还一直产生新的子进程,就会有大量僵尸进程产生,会存留部分PCB在内存中,必须要处理僵尸进程
"""

import os,sys

pid = os.fork()
if pid < 0:
    print("Error")
elif pid == 0:
    print("Child PID:",os.getpid())
    sys.exit(2)
else:
    """
    os.wait() 处理僵尸进程
    """
    pid,status = os.wait() # 阻塞函数,会等待子进程退出再自动处理僵尸 ,弊端,必须子进程先执行完,父进程结束这里的阻塞才能向后运行
    print("pid:",pid)
    print("statis:",status) # child退出状态*256 --结果2*256=512

    while True:  # 父进程不退出
        pass