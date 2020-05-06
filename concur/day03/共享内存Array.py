from multiprocessing import Process,Array

# shm = Array('i',[1,2,3,4]) # 'i' 表示列表中元素类型整数

shm = Array('i',5) #初始开辟五个整型空间0 输出结果
# 0
# 0
# 0
# 0
# 1000

def fun():
    # array创建的共享内存对象可迭代
    for i in shm:
        print(i)
    shm[1] = 1000
p = Process(target=fun)
p.start()
p.join()
print(shm[1])

shm = Array('c',b'hello')
def fun():
    # array创建的共享内存对象可迭代
    for i in shm:
        print(i)
    shm[0] = b'H'
p = Process(target=fun)
p.start()
p.join()
print(shm[0])
print(shm.value) # value 只能用来打印字节串 可以使用obj.value直接打印共享内存中的字节串
