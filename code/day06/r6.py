"""
统计字符串字符出现的次数
首先思考结果是什么类型，a出现一次，c出现两次--->"a": 1   "c": 2,然后确定使用字典
"""

str01 = "abcdefce"
dict01 = {}

for item in str01:
    if item not in dict01:
        dict01[item] = 1
    else:
        dict01[item] += 1
for item, value in dict01.items():
    print("%s出现过的次数是：%d" % (item, dict01[item]))