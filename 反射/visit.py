# -*- coding: utf-8 -*-
# @Author   : klaus
# @time     : 2020/5/11 22:47
# @File     : visit.py
# content   ： python的反射
# @Softwore : PyCharm

import commons

def fun():
    inp = input("请输入访问的url： ")
    # 代码1  low
    # if inp == "login":
    #     commons.login()
    # elif inp == "logout":
    #     commons.logout()
    # elif inp == "home":
    #     commons.home()
    # else:
    #     print("404")

    # 方式2 有缺陷
    # fu = getattr(commons,inp,None)
    # if fu is None:
    #     print("404")
    #     return
    # fu()

    # 方式3
    # if hasattr(commons,inp):
    #     fu = getattr(commons, inp)
    #     fu()
    # else:
    #     print("404")

    # 方式4
    getattr(commons,inp)() if hasattr(commons,inp) else print("404")

def run():
    """
    动态的import 模块
    obj = __import__(modules)  等价于  import commons
    对于lib.xxx.xxx.xxx这一类的模块导入路径，__import__默认只会导入最开头的圆点左边的目录，也就是“lib” 加上fromlist = True参数即可！
    """
    inp = input("请输入访问的url： ").strip()
    modules, func = inp.split("/")
    #obj = __import__("lib." + modules, fromlist=True)
    obj = __import__(modules)

    if hasattr(obj,func):
        func = getattr(obj,func)
        func()
    else:
        print("404")

if __name__ == '__main__':
    #fun()

    run()