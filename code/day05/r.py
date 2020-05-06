# 逛论坛，查看utf-8和utf-16区别

# for i in range(10,0,-1):
#     print(i)

# list01 = list("我是齐天大圣")
# print(list01)

list01 = ["我", "是", "齐", "天","大","圣"]
# 正向索引 0 1 2 3 4 5
# 反转序列
# 第一种  5 4 3 2 1 0
# for index in range(len(list01)-1,-1,-1):
#     print(list01[index])
# 第二种 -1 -2 -3 -4 -5 -6
for index in range(-1,-len(list01)-1,-1):
    print(list01[index])
