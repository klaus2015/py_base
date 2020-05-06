# for r in range(3): # 外层循环控制行
#     for c in range(4): # 内层循环控制列
#         print("*", end = " ")
#     print()
# * * * *
# * * * *
# * * * *



# for r in range(4):
#     for c in range(6):
#         if c % 2 == 1:
#             print("#", end = " ")
#         else:
#             print("*", end = " ")
#     print()

# for r in range(4):      # 0 1 2 3  推理很重要
#     for c in range(r+1):# 1 2 3 4
#         print("*", end=" ")
#     print()
# *
# * *
# * * *
# * * * *

# 列表中的数字比大小
# list01 = [3,80,45,5,7,1]
# for r in range(len(list01)-1):
#     for c in range(r+1,len(list01)):
#         if list01[r] < list01[c]:
#             list01[r], list01[c] = list01[c], list01[r]
# print(list01) # [80, 45, 7, 5, 3, 1]

# 退出来多个循环，使用标记
# result = False
# list02 = [3,80,45,4,80,3]
# for r in range(len(list02)-1):
#     for c in range(r+1,len(list02)):
#         if list02[r] == list02[c]:
#             print("相同的数字是",list02[c])
#             result = True
#             break
#     if result:
#         break
# if not result:
#     print("没有存在相同的")

list01 = [
    [1,2,3,4],
    [5,6,7,8],
    [9,10,11,12],
    [13,14,15,16]
]

# print(list01[1][2])
# for item in list01[2]:
#     print(item)
# for r in range(len(list01)):
#     print(list01[r][0])
result = []
for r in range(4):
    line = []
    result.append(line)
    for c in range(4):
        line.append(list01[c][r])
print(result)