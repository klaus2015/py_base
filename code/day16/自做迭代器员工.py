class Employee:
    pass

class EmployeeManager:
    def __init__(self):
        self.__employee = []

    def add_employee(self,emp):
        self.__employee.append(emp)

    def __iter__(self):
        return EmployeeIterator(self.__employee)

class EmployeeIterator:
    def __init__(self,target):
        self.target = target
        self.index = 0

    def __next__(self):
        if self.index > len(self.target) - 1:
            raise StopIteration
        temp = self.target[self.index]
        self.index += 1
        return temp

e = EmployeeManager()
e.add_employee(Employee())
e.add_employee(Employee())
e.add_employee(Employee())

for item in e:
    print(item)


iterator = e.__iter__()
while True:
    try:
        item = iterator.__next__()
        print(item)
    except StopIteration:
        break