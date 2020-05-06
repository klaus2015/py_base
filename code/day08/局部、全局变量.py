# 利用全局变量统计函数调用次数
count = 0
def fun01():
    global count
    count += 1
    pass

fun01()
fun01()
fun01()
fun01()
fun01()
fun01()
print("调用了%d" % count)