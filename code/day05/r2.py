"""
在控制台种输入你喜欢的西游记中的人物，
输入空字符串后打印每个人物（逐行打印）

"""

# list01 = []
# while True:
#     str_input = input("输入西游记的人物： ")
#     if str_input == '':
#         break
#     list01.append(str_input)
# for item in list01:
#     print(item)


# score_list = []
# while True:
#     str_score = input("请输入所有学生的成绩： ")
#     if str_score == "":
#         break
#     score_list.append(int(str_score))
#
# for item in score_list:
#     print(item)
#
# print("最高分" + str(max(score_list)))
# print(min(score_list))
# print(sum(score_list) / len(score_list))

list_name = []


# 我的代码
while True:
    name = input("请输入学生的姓名： ")
    if name == "":
        break
    if name in list_name:   # name in list
        print("姓名重复输入")
    else:
        list_name.append(name)

for index in range(len(list_name)-1,-1,-1):


    print(list_name[index])

# 老师的代码
while True:
    name = input("请输入学生的姓名： ")
    if name == "":
        break
    if name not in list_name:
        list_name.append(name)
    else:
        print("姓名重复输入")


for index in range(len(list_name)-1,-1,-1):
# 第二种方法for index in range(-1, -len(list_name)-1, -1):
    print(index)
    print(list_name[index])

