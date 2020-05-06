# 练习:定义敌人类(姓名，攻击力10 -- 50，血量100 -- 200)
#    创建一个敌人对象，可以修改数据，读取数据。

class Enemy:
    def __init__(self,name,atk,hp):
        self.name = name
        self.atk = atk
        self.hp = hp

    def get_atk(self):
        return self.__atk

    def set_atk(self,value):
        if 10 < value < 50:
            self.__atk = value
        else:
            raise ValueError("不要")
    atk = property(get_atk,set_atk)

    def get_hp(self):
        return self.__hp

    def set_hp(self,value):
        if 100 < value < 200:
            self.__hp = value
        else:
            raise ValueError("血量错误")
    hp = property(get_hp,set_hp)


en01 = Enemy("灭霸",20,150)
en01.atk = 40
print(en01.atk)



