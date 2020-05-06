class Student:
    def __init__(self,name, age, score, sex):
        # 创建实例对象
        self.name = name
        self.age = age
        self.score = score
        self.sex = sex

    def print_info(self):
        # 调用实例变量
        print("%s的年龄是%d,成绩是%d,性别是%s" % (self.name, self.age,self.score,self.sex))

    def check_name():
        for item in list01:
            if item.name == "苏大强":
                item.print_info()


# list_student_info = []
# while True:
#     name = input("请输入姓名：")
#     if name == "":
#         break
#     age = int(input("请输入年龄："))
#     score = int(input("请输入成绩："))
#     sex = input("请输入性别：")
#     student = Student(name,age,score,sex)
#     stu_info = student         #  关键 将实例对象组成一个列表
#     list_student_info.append(stu_info)
#
# for stu in list_student_info:
#     stu.print_info()

list01 = [
    Student("赵敏", 28, 100, "女"),
    Student("苏大强", 68, 62, "男"),
    Student("无极", 28, 70, "男"),
    Student("张三丰", 130, 96, "女")

]


# def check_name():
#     for item in list01:
#         if item.name == "苏大强":
#             return item
# stu = check_name()
# print(stu.name, stu.age)


# 找出性别是女的所有人
# 我的代码
# list02 = []
# def find02():
#     for item in list01:
#         if item.sex == "女":
#             list02.append(item)
#
# stuwom = find02()
# for item in list02:
#     print(item.name, item.age)



# 老师的
# def find02():
#     # list02 = []
#     # for item in list01:
#     #     if item.sex == "女":
#     #         list02.append(item)
#     # return list02
#     return [item for item in list01 if item.sex == "女"]
#
# stuwom = find02()
# for item in stuwom:
#     print(item.name, item.age)

# 找出年龄大于30的人
# def find03():
#     count = 0
#     for item in list01:
#         if item.age >=30:
#             count += 1
#     return count
#
# result = find03()
# print(result)


# 将成绩归0
# def score_default_zeero():
#     for item in list01:
#         item.score = 0
# score_default_zeero()
# for item in list01:  # 许特别注意list01,不能直接打印
#     print(item.name,item.score)

# 找出所有人的名字
# def get_name():
#     # result = []
#     # for item in list01:
#     #     result.append(item.name)
#     # return result
#     return [item.name for item in list01]
# list_name = get_name()
# print(list_name)
# for item in list_name:
#     print(item)


# 练习6 查找年龄最大的

def get_max_age():
    max_age = list01[0].age
    for item in list01:
        if max_age < item.age:
            max_age = item.age
    return max_age


result = get_max_age()
print(result)
print(list01[0].age)
