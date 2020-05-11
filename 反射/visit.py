# -*- coding: utf-8 -*-
# @Author   : klaus
# @time     : 2020/5/11 22:47
# @File     : visit.py
# @Softwore : PyCharm

import commons

def fun():
    inp = input("请输入访问的url： ")
    # if inp == "login":
    #     commons.login()
    # elif inp == "logout":
    #     commons.logout()
    # elif inp == "home":
    #     commons.home()
    # else:
    #     print("404")
    fu = getattr(commons,inp,None)
    if fu is None:
        print("404")
        return
    fu()

if __name__ == '__main__':
    fun()