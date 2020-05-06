# 可变／不可变类型在传参时的区别
def fun01(a):
    a[0] = 100

list01 = [1]
fun01(list01)
print(list01[0])

def fun04(a):
    a[1] = [200]

list01 = [1,[2,3]]
fun04(list01)
print(list01[1])