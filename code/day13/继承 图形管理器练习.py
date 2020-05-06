"""
    定义图形管理器类
        1. 管理所有图形
        2. 提供计算所有图形总面积的方法

    具体图形:
        圆形(pi × r ** 2)
        矩形(长*宽)
        ...

    测试：
        创建1个圆形对象，1个矩形对象，添加到图形管理器中.
        调用图形管理器的计算面积方法，输出结果。

    要求：增加新图形，不修改图形管理器的代码.
    体会：面向对象三大特征：
            封装/继承/多态
         面向对象设计原则：
            开闭/单一/倒置

"""

class GraphManage:
    def __init__(self):
        self.map_list = []

    def add_map(self,map):
        if isinstance(map,Graph):
            self.map_list.append(map)


    def output_area(self):
        total_area = 0
        for item in self.map_list:
            total_area += item.calculate()
        return total_area




class Graph:

    def calculate(self):

        pass

#--------------------------------------------------------------------------------------------------------
class Round(Graph):
    def __init__(self,r):
        self.r = r

    def calculate(self):
        return 3.14 * self.r **2

class RectAngle(Graph):
    def __init__(self,length,width):
        self.length = length
        self.width = width

    def calculate(self):
        return self.length * self.width


g = GraphManage()
r01 = Round(4)
rc01 = RectAngle(4,5)
g.add_map(r01)
g.add_map(rc01)
print(g.output_area())