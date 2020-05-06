count = 0
# while count < 3:
#     str_score = input("请输入成绩：")
#     if str_score == ' ':
#         break
#     elif int(str_score) > 100 or int(str_score) < 0:
#         count += 1
#         print("输入有误")
#     elif 90 <= int(str_score):
#         print("优秀")
#     elif 80 <= int(str_score):
#         print("良好")
#     elif 60 <= int(str_score):
#         print("及格")
#     else:
#         print("不及格")
# else:  # while 条件不满足执行这里
#     print("成绩错误过多")


while count < 3:
    str_score = input("请输入成绩：")
    if str_score == ' ':
        break # 这里break不会执行36行else语句
    elif int(str_score) > 100 or int(str_score) < 0:
        count += 1
        print("输入有误")
    elif 90 <= int(str_score):
        print("优秀")
    elif 80 <= int(str_score):
        print("良好")
    elif 60 <= int(str_score):
        print("及格")
    else:
        print("不及格")
else:
    print("成绩错误过多")