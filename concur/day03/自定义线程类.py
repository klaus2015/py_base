"""
    自定义线程类
"""
from threading import Thread

# 自定义线程类
class ThreadClass(Thread):
    def __init__(self,*args,**kwargs):
        self.attr = args[0]
        super().__init__() # 加载父类__init__

    def f1(self):
        print("step1")
    def f2(self):
        print("step2")
    def run(self):
        self.f1()
        self.f2()

t = ThreadClass('abc')
t.start() # 自动运行run
t.join()