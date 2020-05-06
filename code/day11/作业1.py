"""
    3. 请用面向对象思想，描述以下场景：
    张无忌　教　赵敏　九阳神功
    赵敏　教　张无忌　化妆
    张无忌　上班　挣了　10000
    赵敏　上班　挣了　6000
    思考：变化点是数据的不同还是行为的不同。

    教 是 张无忌和赵敏的行为,即属于张无忌和张无忌的类中的方法
    如果 教 的具体实现细节很复杂,要把 教的具体方法提出去 做成一个类,但是教还在 Person中,
    上班  也是 张无忌和赵敏的行为
    People 是一个总的负责,


"""


class People:
    def __init__(self, name, skill):
        self.name = name
        self.skill = skill
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self,value):
        self.__name = value

    def teach(self,person):
        print(self.name,"教",person.name,self.skill)

class Work:

    def __init__(self,work,salary):
        self.work = work
        self.salary = salary

    @property
    def work(self):
        return self.__work

    @work.setter
    def work(self,value):
        self.__work = value

    def earn_money(self,person):
        print(person.name,self.work,"挣了%d" % self.salary)
zwj = People("张无忌","九阳神功")
zm = People("赵敏","化妆")
wz = Work("工作",10000)
wm = Work("工作",6000)
zwj.teach(zm)
zm.teach(zwj)
wz.earn_money(zwj)
wm.earn_money(zm)


