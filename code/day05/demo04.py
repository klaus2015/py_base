"""
    str --> list
    练习:exercise08.py
"""

str01 = "张无忌-赵敏-周芷若"
print(str01)
list_result = str01.split("-")
print(list_result)

str02 = "-".join(list_result)
print(str02)
