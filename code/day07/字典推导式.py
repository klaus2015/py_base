list01 = ["无极", "赵敏", "周芷若"]
list02 = [101, 102, 103]
dict01 = {}
dict03 = {}
for item in list01:
    dict01[item] = len(item)
print(dict01)

dict02 = {item:len(item) for item in list01}
print(dict02)
# 通过索引在多个列表中同时获取元素
for i in range(3):

    dict03[list01[i]] = list02[i] # 索引相同，所以用相同的一个索引即可

print(dict03) # {'无极': 101, '赵敏': 102, '周芷若': 103}
list03 = []
for k, v in dict03.items():
    list03.append((k, v))
print(list03)
list04 = [(k,v) for k, v in dict03.items()]
print(list04)


