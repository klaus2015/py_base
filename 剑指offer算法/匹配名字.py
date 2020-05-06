import re


f = open('names')
data = f.read()


f.seek(0)
first_name = []
for name in f:
    first_name.append(name[0])
# print(first_name)
first_name = list(set(first_name))
# print(first_name)

list_each_name = {}
for i in first_name:

    result = re.findall(r'%s\w+'%i,data)
    print(result)
    list_each_name[i] = len(result)
# list_each_name = sorted(list_each_name,reverse=True)
print(list_each_name)
for item in list_each_name:
    print(item,"出现了",len(result),"次")










