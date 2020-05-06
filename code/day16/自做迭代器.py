# 练习：图形管理器记录多个图形
#      迭代图形管理器对象

class GraphicManager:
    """
        图形管理器,可迭代对象,参与for
    """
    def __init__(self):
        self.__graphics = []

    def add_graphic(self, graphic):
        self.__graphics.append(graphic)

    def __iter__(self):

        # for item in self.__graphics:
        #     yield item
        number = 0
        while number < len(self.__graphics):
            yield self.__graphics[number]
            number += 1


class Graphic:
    pass
    # def calculate_area(self):
    #     # 如果子类不重写，则异常.
    #     raise NotImplementedError()

# class GraphicIterator:
#     """
#         图形迭代器 获取下一个数据
#     """
#     def __init__(self,target):
#         self.target = target
#         self.index = 0
#
#     def __next__(self):
#         if self.index > len(self.target)-1:
#             raise StopIteration
#         item = self.target[self.index]
#         self.index += 1
#         return item



manager = GraphicManager()
manager.add_graphic(Graphic())
manager.add_graphic(Graphic())
manager.add_graphic(Graphic())
# for item in manager:

iterator = manager.__iter__()

while True:
    try:
        item = iterator.__next__()
        print(item)
    except StopIteration:
        break
