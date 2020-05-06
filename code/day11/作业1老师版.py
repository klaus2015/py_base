"""
    3. 请用面向对象思想，描述以下场景：
    张无忌　教　赵敏　九阳神功
    赵敏　教　张无忌　化妆
    张无忌　上班　挣了　10000
    赵敏　上班　挣了　6000
    思考：变化点是数据的不同还是行为的不同。

    教 是 张无忌和赵敏的行为,即属于张无忌和张无忌的类中的方法
    上班  也是 张无忌和赵敏的行为


"""


class People:
    def __init__(self, name):
        self.name = name

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self,value):
        self.__name = value

    def teach(self,other,skill):
        print(self.name,"教",other.name,skill)

    def work(self, money):
        print(self.name,"上班挣了", money)

zwj = People("张无忌")
zm = People("赵敏")
zwj.teach(zm,"九阳神功")
zm.teach(zwj,"画眉")
zwj.work(10000)
zm.work(6000)

