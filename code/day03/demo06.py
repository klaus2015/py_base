"""
    循环语句
        while 条件:
            循环体
    练习:exercise08.py
"""

# 死循环：循环条件永远是满足的。
# prompt = "\n请输入美元： "
# prompt += "\n输入q表示结束"
while True:
    usd = input("请输入美元：")
    if usd == 'q':
        break
    print(int(usd) * 6.9)

# while True:
#      usd = input(prompt)
#      if usd == 'q':
#          break
#      print(int(usd) * 6.9)
