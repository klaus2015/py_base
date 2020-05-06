
# 选择排序
list01 = [10,9,4,3,5]
def select():
    for r in range(len(list01)-1):
        min = r
        for c in range(r+1,len(list01)):
            if list01[min] > list01[c]:
                min = c
        if min != r:
            list01[r],list01[min] = list01[min],list01[r]

select()
print(list01)

#插入排序
def insert():
    for i in range(4):




