list01 = [1,55,40,80,9]
def my_enum(iterable_target):
    for index in range(len(iterable_target)):
            yield (index,iterable_target[index])

for item in my_enum(list01):
    print(item)
list02 = ["孙悟空","猪八戒","唐僧","沙僧","heh"]
list03 = [101,102,103,104,]
def my_zip(iterable_target1,iterable_target2):


for item in my_zip(list02,list03):
    print(item)
zip()
