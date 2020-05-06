list01 = [4,5,566,7,8,10]

#方法1
list02 = []
for item in list01:
    if item % 2 == 0:
        list02.append(item)
print(list02)

# 方法2
list03 = [item for item in list01 if not item % 2]
print(list03)

#方法3
def get_odd(target):
    for item in list01:
        if item % 2 == 0:
            yield item
g01 = get_odd(list01)
for item in g01:
    print(item)

# 方法4
def get_even02():
    list02 = []
    for item in list01:
        if item % 2 == 0:
            list02.append(item)
    return list02
result = get_even02()
for item in result:
    print(item)


a = [yield item for item in list01 if not item % 2]
print(a)