from common.list_helper import *
list01 = [43, 4, 5, 5, 6, 7, 87]


def find(func_condition,list_target):
    for item in list_target:
        if func_condition(item):
            yield item


def condition01(item):
    return item % 2 == 0


def condition02(item):
    return item > 10


def condition03(item):
    return 10 <= item <= 50

# for item in ListHelper.find_all(list01,condition01):
#     print(item)


for item in ListHelper.find_all(list01,lambda item: item % 2 ==0):
    print(item)

for item in ListHelper.find_all(list01,lambda item: item > 10):
    print(item)

for item in ListHelper.find_all(list01,lambda item: 10<item<50):
    print(item)