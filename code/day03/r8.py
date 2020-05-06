"""

在控制台中获取年龄
如果小于０岁，打印输入有误
如果一个人的年龄小于2岁，就打印一条消息，指出他是婴儿。
如果一个人的年龄为2（含）～13岁，就打印一条消息，指出他是儿童。
如果一个人的年龄为13（含）～20岁，就打印一条消息，指出他是青少年。
如果一个人的年龄为20（含）～65岁，就打印一条消息，指出他是成年人。
如果一个人的年龄超过65（含）岁～150岁，就打印一条消息，指出他是老年人。
150岁以上，打印"那不可能"
"""
while True:
    str_age = (input("请输入你的年龄： "))
    if str_age == "q":
        break
    else:
        age = int(str_age)
        if age < 0:
            print("输入有误！")
        elif age < 2:
            print("他是婴儿！")
        elif age < 13:
            print("他是儿童！")
        elif age < 20:
            print("他是青少年！")
        elif age < 65:
            print("他是成年人！")
        elif age >= 65:
            if age < 150:
                print("他是老年人！")
            else:
                print("不可能")