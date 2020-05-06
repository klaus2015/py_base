import time

# def execute_time(func):
#     def wrapper(*args, **kwargs):
#         start_time = time.time()
#         func(*args, **kwargs)
#         t = time.time() - start_time
#         print("运行了%f" % t)
#     return wrapper
"""
fun01执行喽
运行了2.002108
fun02执行了,参数是 10000
运行了1.000213
"""

def print_execute_time(func):
    def wrapper(*args, **kwargs):
        # 记录调用前的时间
        start_time = time.time()
        result = func(*args, **kwargs)
        # 记录调用后的时间
        execute_time = time.time() - start_time
        print("执行时间是：", execute_time)
        return result

    return wrapper
"""
fun01执行喽
执行时间是： 2.0020740032196045
fun02执行了,参数是 10000
执行时间是： 1.0001652240753174
"""

@print_execute_time
def fun01():
    time.sleep(2)
    print("fun01执行喽")

@print_execute_time
def fun02(a):
    time.sleep(1)
    print("fun02执行了,参数是",a)


fun01()
fun02(10000)



