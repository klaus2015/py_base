"""
gevent_ 协成模块示例
"""

import gevent
from gevent import monkey  # 导入monkey
#在gevent协程中,协程只有遇到gevent指定类型的阻塞才能跳转到其他协程,因此,我们
#希望将普通的IO阻塞行为转换为可以触发gevent协程跳转的阻塞,以提高执行效率
monkey.patch_time()  # 运行脚本 需要在time模块导入前,这时time模块所对应的阻塞就会变成gevent跳转的阻塞
from time import sleep

# 协程函数
def foo(a,b):
    print("Runnning foo...",a,b)  # 生成的协程对象遇到gevent.joinall([f,b])开始执行,下面遇到g_sleep(2)阻塞
                                    #会自动取查看有没其他可以执行的协程,执行到print("Runnning bar...")
                                    #然后又阻塞,这时两个地方都在阻塞,协程会等待2秒,执行Foo,然后等待1s执行Bar,
                                    # 整个程序三秒执行完毕,效率高
    # gevent.sleep(2)
    sleep(2)
    print("Foo again")
def bar():
    print("Runnning bar...")
    # gevent.sleep(3)
    sleep(3)
    print("Bar again")

# 生成协程对象
f = gevent.spawn(foo,1,2)  # 准备好要执行,需要一个触发他的执行条件,即阻塞行为
b = gevent.spawn(bar)
# sleep(5)
# gevent.sleep(5) # 遇到gevent指定的阻塞行为时才执行,或会自动在协程之间进行跳转
gevent.joinall([f,b])  # 阻塞等待f和b两个协程执行完毕
