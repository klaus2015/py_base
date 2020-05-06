# 练习：图形管理器记录多个图形
#      迭代图形管理器对象

class Graphic:
    pass


class GraphicManager:
    """
        图形管理器，可迭代对象(参与for)
    """
    def __init__(self):
        self.__graphics = []

    def add_graphic(self, graphic):
        self.__graphics.append(graphic)

    def __iter__(self):
        for item in self.__graphics:
            yield item





manager = GraphicManager()
manager.add_graphic(Graphic())
manager.add_graphic(Graphic())
manager.add_graphic(Graphic())
# for item in manager:
#     print(item)

iterator = manager.__iter__()
while True:
    try:
        item = iterator.__next__()
        print(item)
    except StopIteration:
        break
# 1 创建在对象内部创建__iter__()方法,返回迭代器对象,然后在迭代器里创建__next__()方法,
# 调用_next__()方法来获取下一个值------对象即可变成可迭代的
# 调用对象的__iter__()方法会生产迭代器对象,调用迭代器对象的__next__()方法
# 会返回对象的下一个值,直至产生StopIteration.

#2 将yield直接放在对象内部创建的__iter__()方法中(方法即变成生成器函数,调用生成器函数会自动创建创建迭代器对象,
# 迭代器中即有__next__()方法),
# yield 的作用: 将下列代码改为迭代器模式的代码
#1. 生成迭代器对象的大致规则---1将yield以前的语句定义在next方法中,2将yield后面的数据作为next方法返回值

# 3含有yield语句的函数，返回值为生成器对象,用生成器函数将返回一个生成器对象，不执行函数体
#   1调用生成器函数会自动创建迭代器对象(),2调用迭代器对象的__next__()方法时才执行生成器函数,
#   3每次执行到yield语句时返回数据，暂时离开,4待下次调用__next__()方法时继续从离开处继续执行
# 生成器原理
class MyGenerator:
    # 生成器 = 可迭代对象 + 迭代器
    def __init__(self, stop_value):
        self.begin = 0
        self.stop_value = stop_value

    def __iter__(self):
        return self # 本来是可迭代对象调用此方法返回迭代器对象,
                    # 现在返回的是自身self,self=self(可迭代对象) + 迭代器对象

    def __next__(self):
        if self.begin >= self.stop_value:
            raise StopIteration

        temp = self.begin
        self.begin += 1
        return temp