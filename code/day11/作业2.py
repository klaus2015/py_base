"""
    4. 请用面向对象思想，描述以下场景：
    玩家(攻击力)攻击敌人(血量)，敌人受伤(掉血)，还可能死亡(掉装备，加分)。
    敌人(攻击力)攻击玩家，玩家(血量)受伤(掉血/碎屏),还可能死亡(游戏结束)。

"""
class Player:
    def __init__(self,name,atk,hp):
        self.name = name
        self.atk = atk
        self.hp = hp

    def attack(self):
        print("玩家攻击敌人")

    def player_death(self):
        if self.hp == 0:
            print("游戏结束")

class Enemy:
    def __init__(self,name,atk,hp):
        self.name = name
        self.atk = atk
        self.hp = hp

    def enemy_under_attack(self):
        print("死亡，掉装备")

class Under_Attack:

    def under_attack(self,p1,p2):
        loose_hp = p1.hp - p2.atk
        print(p1.name,"受到攻击，血量减少了%d" % loose_hp)
ply = Player("英雄",80,200)
eny = Enemy("小怪",40,100)
un_attack = Under_Attack()
un_attack.under_attack(ply,eny)
ply.player_under_attack()

un_attack.under_attack(eny,ply)
eny.enemy_under_attack()




