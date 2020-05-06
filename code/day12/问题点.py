# 属性有了行为,才能产生成独立的类,没有了产生行为及时单一的属性
# 类  区分行为的不同  ---> 不同行为即为不同的类
# 一个类中变化的地方抽离出去,使他的改变减少对前一个类的影响,即两个变化的东西,不要放在一起
# 类变量的调用,类名调用和实例调用的区别
class A():
    def __init__(self):
        self.__data=[] #翻译成 self._A__data=[]

    def add(self,item):
        self.__data.append(item) #翻译成 self._A__data.append(item)

    def printData(self):
        print(self.__data) #翻译成 self._A__data

a=A()
a.add("haha")
a.add("python")
a.printData()