class Baby:
    def __init__(self, name, weight, sex):
        self.name = name
        self.weight = weight
        self.sex = sex

    def cry(self):
        print(self.name + " is often cry!")

    def eat(self):
        print(self.name + " eat a lot")

baby1 = Baby("花花", 6.6, "女")
print(baby1.name)
baby1.cry()


baby2 = Baby("舒克", 18, "男")
print(baby2.sex)
baby2.eat()


class Car:
    def __init__(self, model, colour, speed=150):
        self.model = model
        self.colour = colour
        self.speed = speed

    def drive(self):
        print(self.model + "drive very fast!")

car01 = Car("aodi", "black", 200)
print(car01.model)
print(car01.speed)
car01.drive()

car02 = Car("BMW", "white", )
print(car02.speed)
car02.drive()


