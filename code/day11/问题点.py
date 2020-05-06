"""
    封装设计思想
        需求：老张开车去东北
"""


class People:
    def __init__(self, name):
        self.name = name

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    def go_somewhere(self,type,str_pos):
        print(self.name,"去",str_pos)
        type.run(str_pos)

class Car:
    # def __init__(self,car):
    #     self.car = car
    #
    # @property
    # def car(self):
    #     return self.__car
    #
    # @car.setter
    # def car(self,value):
    #     self.__car = value

    def run(self,str_pos):
        print("车开到:", str_pos)

lz = People("老张")
c = Car()
lz.go_somewhere(c,"东北")


