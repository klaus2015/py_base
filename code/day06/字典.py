# dict01 = {}
# while True:
#     name = input("请输入商品名称： ")
#     if name == '':
#         break
#     price = int(input("请输入商品价格： "))
#     dict01[name] = price
# print(dict01)
# for key ,value in dict01.items():
#     print("输入的%s价钱是%d" % (key, value))


# 字典镶嵌列表
# dict_students_info = {}
# while True:
#     name = input("请输入学生名称： ")
#     if name == '':
#         break
#     age = int(input("请输入年龄： "))
#     score = int(input("请输入成绩： "))
#     sex = input("输入性别： ")
#
#     dict_students_info[name] = [age, score, sex]  # 直接创建字典的键对应的值--->列表
#
# print(dict_students_info)

# 字典镶嵌字典
# dict_students_info = {}
# while True:
#     name = input("请输入学生名称： ")
#     if name == '':
#         break
#     age = int(input("请输入年龄： "))
#     score = int(input("请输入成绩： "))
#     sex = input("输入性别： ")
#
#
#     dict_students_info[name] = {"age": age, "score": score, "sex": sex} # 直接创建字典键对应的值-->字典
#
# print(dict_students_info)


# 列表镶嵌字典 获取第一个和最后一个学生的录入信息
# 在这个列表中,所有字典的结构都相同,因此你可以遍历这个列表,并以相同的方式处理其中的每个字典
list_info = []

while True:
    name = input("请输入学生名称： ")
    if name == '':
        break
    age = int(input("请输入年龄： "))
    score = int(input("请输入成绩： "))
    sex = input("输入性别： ")
    dict_students_info = {"name": name, "age": age, "score": score, "sex": sex} # 直接创建字典，当做一个元素
    list_info.append(dict_students_info)                                         # 添加到列表中
for dict in list_info:
    print(dict)
# 获取第一个学生信息
dict_students_info = list_info[0]
print("第一个录入的是：%s,年龄是%d,成绩是%d,性别是%s" % (dict_students_info["name"],
        dict_students_info["age"],dict_students_info["score"],dict_students_info["sex"]))
