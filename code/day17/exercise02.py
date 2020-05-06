"""
# 练习: 定义生成器函数my_zip,实现下列现象.
# 将多个列表的每个元素合成一个元组.
list02  = ["孙悟空","猪八戒","唐僧","沙僧"]
list03  = [101,102,103,104]
for item in zip(list02,list03):
    print(item)
"""

# 练习: 定义生成器函数my_zip,实现下列现象.
# 将多个列表的每个元素合成一个元组.
list02  = ["孙悟空","猪八戒","唐僧","沙僧","小白龙"]
list03  = [101,102,103,104]

# def my_zip(list01,list02):
#     for i in range(len(list01)):
#         yield (list01[i],list02[i])
#
# for item in my_zip(list02,list03):
#     print(item)
print("+++++++++++++++++++++++++++++++++++++++++")
# (扩展)
def my_zip2(*args):
    # 根据星号元组形参args第一个参数的长度生成索引len(args[0])
    min_list = min(args,key=lambda item:len(item))
    for i in range(len(min_list)):
        list_tuple = []
        for item in args:
            list_tuple.append(item[i])
        yield tuple(list_tuple)


for item in my_zip2(list02,list03):
    print(item)

def my_zip2(*args):
    # 根据星号元组形参args第一个参数的长度生成索引len(args[0])
    min_list = min(args,key=lambda item:len(item))
    result = []
    for i in range(len(min_list)):
        list_tuple = []
        for item in args:
            list_tuple.append(item[i])
        result.append(tuple(list_tuple))
    return result
re = my_zip2(list02,list03)
print(re)