"""
Event 线程互斥演示
"""

from threading import Thread,Event

s = None # 用于通信

def yang():
    print("杨子荣前来拜山头")
    global s
    s = "天王盖地虎"  # 修改s

t = Thread(target=yang)
t.start()

print("说对口令就是自己人")
if s == '天王盖地虎':  # 验证s   修改和验证的速度谁先执行不一定,可能被打死,也可能验证通过
    print("宝塔镇河妖")
    print("是队友")
else:
    print("打死他...")

t.join()
