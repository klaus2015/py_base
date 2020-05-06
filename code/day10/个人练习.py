"""
    "4. 定义敌人类
    --　数据:姓名,血量,基础攻击力,防御力
    --　行为:打印个人信息

   创建敌人列表(至少４个元素),并画出内存图。
   查找姓名是"灭霸"的敌人对象
   查找所有死亡的敌人
   计算所有敌人的平均攻击力
   删除防御力小于10的敌人
   将所有敌人攻击力增加50

"""
class Enemy:
    """

    敌人类
    """

    def __init__(self,name,hp,basci_damage,defensive):
        self.name = name
        self.hp = hp
        self.atk = atk
        self.defense = defense

    def print_info(self):
        print("%s的血量是%d,初始攻击力为%d,防御力为%d" % (self.name, self.hp, self.atk, self.defense))

list_enemy = [
    Enemy("红骷髅", 200, 50, 5),
    Enemy("灭霸", 500, 150, 20),
    Enemy("海拉", 250, 100, 6.7),
    Enemy("奥创", 0, 100, 12),
    Enemy("蜘蛛侠", 0, 80, 11)
]
# 查找姓名是"灭霸"的敌人对象
def find_thanos():
    for item in list_enemy:
        if item.name == "灭霸":
            return item

result = find_thanos()
# 没找到灭霸返回值为None,所以要加判断
if result:
    print(result.name)
else:
    print("没找到")

# 查找所有死亡的敌人
def find_hp_zero():
    return [item for item in list_enemy if item.hp == 0]

result = find_hp_zero()
for item in result:
    print("死亡的敌人有%s" % item.name)

# 计算所有敌人的平均攻击力
def get_average_attack_power():
    sum_atk = 0
    for item in list_enemy:
        sum_atk += item.atk
    return sum_atk / len(list_enemy)
re = get_average_attack_power()
print(re)

# 删除防御力小于10的敌人
def remove_week_enemy():
    for i in range(len(list_enemy)-1,-1,-1):
        if list_enemy[i].defense < 10:
            del list_enemy[i]

remove_week_enemy()
for item in list_enemy:
    print(item.name)

# 将所有敌人攻击力增加50
def increase_basci_damage():
    for item in list_enemy:
        item.atk += 1.5
increase_basci_damage()
for i in list_enemy:
    print(i.atk)