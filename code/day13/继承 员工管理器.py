class StaffManager:
    """
        员工管理器
    """
    def __init__(self):
        self.__staff_list = []

    @property
    def taff_list(self):
        return self.__staff_list

    def add_employ(self,emp):
        if isinstance(emp,Staff): # 如果传入的是子类,则添加进员工列表
            self.__staff_list.append(emp)

    def calculate_total_salary(self):
        """
            计算员工总工资
        :return: 返回计算结果
        """
        total_salary = 0
        for item in self.__staff_list:
            total_salary += item.calculate_salary()
        return total_salary


class Staff:
    def __init__(self, basic_salary):
        self.basic_salary = basic_salary


    def calculate_salary(self):
        return self.basic_salary


class Programmer(Staff):
    def __init__(self, basic_salary, bonus):
        super().__init__(basic_salary)
        self.bonus = bonus

    def calculate_salary(self):
        # return self.basic_salary + self.bonus          # 这行是直接改变父类的
        return super().calculate_salary() + self.bonus # 扩展父类的方法重写


class Saler(Staff):
    def __init__(self, basic_salary, sales_volume):
        super().__init__(basic_salary)
        self.sales_volume = sales_volume

    def calculate_salary(self):
        return self.basic_salary + self.sales_volume * 0.05


sta = StaffManager()
prog = Programmer(20000,100000)
saler = Saler(5000, 100000)
sta.add_employ(prog)
sta.add_employ(saler)
print(sta.calculate_total_salary())
