"""
    # 练习１：
    在list_helper.py中增加通用的求和方法.
    案例1:计算敌人列表中所有敌人的总血量.
    案例2:计算敌人列表中所有敌人的总攻击力.
    案例3:计算敌人列表中所有敌人的总防御力.
    步骤：
    实现具体功能/提取变化/提取不变/组合
"""
from common.list_helper import *
class Enemy:
    def __init__(self, name, hp, atk, defense):
        self.name = name
        self.hp = hp
        self.atk = atk
        self.defense = defense

    def __str__(self):
        return "%s--%d--%d--%d" % (self.name, self.hp, self.atk, self.defense)


list01 = [
    Enemy("玄冥二老", 50, 120, 4),
    Enemy("成昆", 0, 70, 5),
    Enemy("谢逊", 0, 85, 6),
    Enemy("灭霸", 100, 100, 10),
]
# re = ListHelper.sum(list01,lambda item: item.hp)
# print(re)
#
# re = ListHelper.sum(list01,lambda item: item.atk)
# print(re)
#
# re = ListHelper.sum(list01,lambda item: item.defense)
# print(re)
#



# re = list(ListHelper.select(list01,lambda item:(item.name,item.hp)))
# print(re)


# def func():
#     if max.atk < item.atk:
#         return max
# def hangdle(item):
#     return item.atk


# re = ListHelper.get_max(list01,lambda item:item.atk)
# print(re)
#
# re = ListHelper.get_max(list01,lambda item: item.hp)
# print(re)
#
# re = ListHelper.get_max(list01,lambda item:item.defense)
# print(re)

# re = ListHelper.ascending_sort(list01,lambda item:item.hp)
# for item in list01:
#     print(item)
# 血量最少的人
re = ListHelper.get_min(list01,lambda item:item.hp)
print(re)

# 攻击力最小的敌人
re = ListHelper.get_min(list01,lambda item:item.atk)
print(re)
print("-------------")
#删除灭霸
# ListHelper.remove_element(list01,lambda item: item.name == "灭霸")
# for item in list01:
#     print(item)
print("-------------")
#删除血量等于0的
# ListHelper.remove_element(list01,lambda item:item.hp == 0)
# for item in list01:
#      print(item)
print("-------------")
# 降序排列攻击
ListHelper.order_reverse(list01,lambda item:item.atk)
for item in list01:
    print(item)