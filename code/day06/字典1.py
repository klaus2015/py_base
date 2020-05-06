"""
在控制点台中录入多个人的喜好

"""
# 列表镶嵌字典
list_hobby = []
while True:
    count = 0
    name = input("请输入姓名： ")
    if name == '':
        break
    while True:
        hobby = input("请输入爱好：")
        if hobby == '':
            break
        dict_hobby = {"name": name, "hobby": hobby}
    list_hobby.append(dict_hobby)
for item in list_hobby:
    print(item)
