"""
    小明在招商银行取钱
    类中存的方法是类承担的动作,银行规定取钱的逻辑,所以取钱的方法在银行

"""


class Peopel:
    def __init__(self, name, money):
        self.name = name
        self.money = money

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    @property
    def money(self):
        return self.__money

    @money.setter
    def money(self, value):
        self.__money = value


class Bank:

    def __init__(self, name, money):
        self.name = name
        self.money = money

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    @property
    def money(self):
        return self.__money

    @money.setter
    def money(self, value):
        self.__money = value

    def taken_money(self, person,value):
        """

        :param person: person
        :param value: value
        :return:
        """
        person.money += value
        self.money -= value
        print(person.name,"取了%d块钱" % value)



xm = Peopel("小明",0)
zsyh = Bank("招商银行",100000)
zsyh.taken_money(xm,5000)
