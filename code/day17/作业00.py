"""
    3. 定义敌人类(姓名,攻击力,防御力,血量)
   创建敌人列表,使用list_helper实现下列功能.
   (1) 查找姓名是"灭霸"的敌人
   (2) 查找攻击力大于10的所有敌人
   (3) 查找活的敌人数量
"""
from common.list_helper import *
class Enemy:
    """

    敌人类
    """

    def __init__(self,name,hp,basic_damage,defensive):
        self.name = name
        self.hp = hp
        self.basic_damage = basic_damage
        self.defensive = defensive

    def __str__(self):
        return "%s,%d,,%d,,%d" % (self.name, self.hp, self.basic_damage, self.defensive)

list_enemy = [
    Enemy("红骷髅", 200, 50, 5),
    Enemy("灭霸", 500, 150, 20),
    Enemy("海拉", 250, 100, 6),
    Enemy("奥创", 0, 100, 12),
    Enemy("蜘蛛侠", 0, 80, 11),
    Enemy("成昆",80,30,10)
]
# re = ListHelper.find_single(list_enemy,lambda item:item.name =="灭霸")
# print(re)
re = ListHelper.find_all(list_enemy,lambda item:item.basic_damage > 10)
# result = list(re)
# for item in result:
#     print(item)
print("-------------")
for item in re:
    print(item)


re = ListHelper.get_count(list_enemy,lambda item:item.hp > 0)
print(re)
# 判断敌人列表中是否存在"成昆"
re = ListHelper.is_exits(list_enemy,lambda item:item.name == "成昆")
print(re)

#判断敌人列表中是否攻击力小于5或者防御力小于10的敌人
re = ListHelper.is_exits(list_enemy,lambda item:item.basic_damage < 5 or item.defensive <10)
print(re)
