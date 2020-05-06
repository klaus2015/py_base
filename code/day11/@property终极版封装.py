# 练习:定义敌人类(姓名，攻击力10 -- 50，血量100 -- 200)
#    创建一个敌人对象，可以修改数据，读取数据。

class Enemy:
    def __init__(self,name,atk,hp):
        self.name = name
        self.atk = atk
        self.hp = hp
    @property  # 创建property对象,只负责拦截读取操作
    def atk(self):
        return self.__atk
    @atk.setter  # 只负责拦截写入操作
    def atk(self,value):
        if 10 < value < 50:
            self.__atk = value
        else:
            raise ValueError("不要")

    @property
    def hp(self):
        return self.__hp
    @hp.setter
    def hp(self,value):
        if 100 < value < 200:
            self.__hp = value
        else:
            raise ValueError("血量错误")



en01 = Enemy("灭霸",20,150)
en01.atk = 40
print(en01.atk)