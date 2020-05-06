"""
multiprocessing 模块创建进程
1. 编写进程函数
2. 生产进程对象
3. 启动进程
4. 回收进程
"""

import multiprocessing as mp
from time import sleep

a = 1

# 进程函数
def fun():
    print("开始一个进程")
    sleep(5)
    global a
    print('a = ',a)
    a = 10000
    print("子进程结束")

# 创建进程对象
p = mp.Process(target = fun)

# sleep(3)
# print("父进程干点事")  放在这里,父进程先执行三秒,然后开始子进程,5秒后结束,总共耗时8秒

p.start() # 启动进程

# 父进程事件
# sleep(1)
# print("父进程干点事")

p.join() # 回收进程
sleep(3)
print("父进程干点事")  # 放在这join()会阻塞,等待子进程执行5秒结束后,再等待3秒执行父进程
                    #join(1)意思为join阻塞1秒后开始执行join下面的内容,而不是等到子进程结束再执行

print('a:',a)

"""
pid = os.fork()
if pid == 0:
    fun()
    os._exit()
else:
    os.wait()
"""