# set01 = set()
# while True:
#     str01 = input("请输入字符串： ")
#     if str01 == "":
#         break
#     set01.add(str01)
# print(set01)


set_manager = {"曹操", "刘备", "孙权"}
set_skill = {"曹操","刘备","关羽","张飞"}
set01 = set_manager & set_skill
print(set01)
set02 = set_manager - set_skill
print(set02)
set03 = set_skill - set_manager
print(set03)
set04 = "张飞" in set_manager
print(set04)


set06 = set_manager | set_skill
list01 = list(set06)
print(len(list01))