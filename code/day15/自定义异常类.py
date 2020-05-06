class HpError(Exception):
    def __init__(self,message,code_line,atk,id):
        super().__init__("攻击力错误啦!!!")
        self.message =message
        self.code_line = code_line
        self.atk = atk
        self.id = id



class Enemy:
    def __init__(self, atk):
        self.atk = atk

    @property
    def atk(self):
        return self.__atk

    @atk.setter
    def atk(self,value):
        if 0<= value <= 100:
            self.__atk = value
        else:
            raise HpError("攻击力错了",21,value,404)

try:
    e01 = Enemy(200)
except HpError as h:
    print("请重新输入整数")
    print(h.atk)



