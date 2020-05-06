# 从多个子类当中(有共同性的行为)抽象出来父类 ,学生会说话,会讲话,老师会讲课,
# 会说话,可以把两个类抽象出人的这个父类,将行为抽象到父类的方法里
# 类型对象指针
# 23种设计模式 python面向对象设计模式
class Car:
    def __init__(self):
        pass

class ElectricCar(Car):
    pass

class ACar(Car):
    pass

c = Car()
ec = ElectricCar()
ac = ACar()
print(type(c))
print(type(ec))

print(Car)
print(ACar)
print(type(ec) == Car)

