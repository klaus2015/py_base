from greenlet import greenlet
def fun1():
    print("执行fun01")
    print("结束fun01")
def fun2():
    print("执行fun0")
    print("结束fun02")

gr1 = greenlet(fun1)
gr2 = greenlet(fun2)
gr1.switch()