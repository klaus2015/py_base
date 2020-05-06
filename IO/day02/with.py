"""
with.py
使用ｗｉｔｈ语句打开文件
"""

with open('day02整体内容') as f: #　生成文件对象
    data = f.read()
    print(data)

# with语句块结束　ｆ对象被自动销毁