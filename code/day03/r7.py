"""
在控制台中获取月份,显示季度,或者提示月份错误

"""
while True:
    mounth = int(input("请输入月份： "))
    if mounth <= 0 or mounth > 12:
        print("月份输入有误！")
    elif mounth <= 3: # elif mounth == 1 or mounth == 2 or mounth ==3:(自己写的，复杂)
        print("季度是：春季")
    elif mounth <= 6:
        print("季度是：夏季")
    elif mounth <= 9:
        print("季度是：秋季")
    else:
        print("季度是：冬季")
