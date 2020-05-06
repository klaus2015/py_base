"""
获取开始值，和结束值，获取中间值


"""
#我的方法1
# begin_number = int(input("输入一个开始值： "))
# end_number = int(input("输入一个结束值： "))
#
# result = 0
# while True:
#     result += 1
#     if begin_number < result < end_number:
#         print(result)

#老师的方法
begin_number = int(input("输入一个开始值： "))
end_number = int(input("输入一个结束值： "))
while begin_number < end_number-1:
    begin_number += 1
    print(begin_number)