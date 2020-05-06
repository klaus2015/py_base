"""
录入成绩，判断等级

"""
#录入成绩
grade = int(input("请输入一个成绩： "))
# 自己的代码 ——————》》if score > 100 or score < 0: 需要首先排除不符合范围内的数字
# if 0 < grade < 60:
#     print("成绩不及格！")
# elif  grade < 80:
#     print("成绩及格！")
# elif grade < 90:
#     print("成绩良好！")
# elif grade <= 100:
#     print("优秀")
# else:
#     print("输入有误")

score = int(input("请输入一个成绩： "))
if score > 100 or score < 0:
    print('输入错误')
elif score >= 90:
    print("优秀")
elif score >= 80:
    print("良好")
elif score >= 60:
    print("及格")
else:
    print("不及格")
