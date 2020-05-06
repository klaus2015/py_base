import asyncio

# 定义协成函数
async def fun1():
    print("start1")
    await asyncio.sleep(2)  # 只能用自身自带的阻塞才有用,换成其他的sleep,或者recv,accept都会报错
    print("end1")

async def fun2():
    print("start2")
    await asyncio.sleep(3)
    print("end2")
