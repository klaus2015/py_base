"""
    4. 请用面向对象思想，描述以下场景：
    玩家(攻击力)攻击敌人(血量)，敌人受伤(掉血)，还可能死亡(掉装备，加分)。
    敌人(攻击力)攻击玩家，玩家(血量)受伤(掉血/碎屏),还可能死亡(游戏结束)。

"""

class Player:
    def __init__(self,atk,hp):

        self.atk = atk
        self.hp = hp

    def attack(self,other):
        print("玩家攻击敌人")
        other.damage(self.atk)

    def damage(self,value):
        print("玩家受伤")
        self.hp -= value
        if self.hp <= 0:
            self.__death()

    def __death(self):
        print("玩家死亡")
        print("游戏结束")


class Enemy:
    def __init__(self, atk, hp):
        self.atk = atk
        self.hp = hp

    def damage(self,value):
        print("敌人受伤")
        self.hp -= value
        if self.hp <= 0:
            self.__death()

    def __death(self):
        print("死亡")
        print("掉装备")
        print("加分")

    def attack(self,other):
        print("敌人攻击玩家")
        other.damage(self.atk)

p01 = Player(100,1000)
e01 = Enemy(10,200)
p01.attack(e01)

