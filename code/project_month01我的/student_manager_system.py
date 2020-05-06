"""
    学生信息管理系统
    项目计划:
            1.完成数据模型类StudentModel
            2.创建逻辑控制类StudentManagerContral


"""
class StudentModel:
    """
        学生数据模型
    """

    def __init__(self,name="",age=0,score=0,id=0):
        """

        :param name: 姓名 str类型
        :param age:  年龄 int类型
        :param score: 分数 int类型
        :param id: 编号(该学生对象的唯一标识)
        """
        self.name = name
        self.age = age
        self.score = score
        self.id = id


class StudentManagerController:
    """
        学生管理控制器,负责管理系统的业务逻辑处理
    """
    # 类变量,表示初始编号
    __init_id = 1000
    def __init__(self):
        self.__stu_list = []


    @property
    def stu_list(self):
        """
        学生列表
        :return:存储学生的列表
        """
        return self.__stu_list


    def add_student(self, stu_info):
        """
            添加一个新学生
        :param stu_info: 没有编号的学生信息
        """
        # self.stu_list.append(stu_info)  也可以
        stu_info.id = self.__generate_id()
        self.__stu_list.append(stu_info)

    def __generate_id(self):
        StudentManagerController.__init_id += 1
        return StudentManagerController.__init_id

    def remove_student(self,id):

        for item in self.__stu_list:
            if item.id == id:
                self.__stu_list.remove(item)
                return True
            return False



    def update_student(self,stu_info):
        """
            修改学生信息

        """
        for item in self.__stu_list:
            if item.id == stu_info.id:
                item.name = stu_info.name
                item.age = stu_info.age
                item.score = stu_info.score
                return True
            return False

class StudentManagerView:
    """
        学生管理器视图
    """

    def __init__(self):
        self.__manager = StudentManagerController()

    def __display_menu(self):
        print("1)添加学生")
        print("2)显示学生")
        print("3)删除学生")
        print("4)修改学生")
        print("5)按照成绩升序显示学生")

    def __select_menu(self):
        item = input("请输入：")
        if item == "1":
            self.__input_student()
        elif item == "2":
            self.__output_students(self.__manager.stu_list)
        elif item == "3":
            self.__delete_student()
        elif item == "4":
            self.__modify_student()
        elif item == "5":
            pass

    def main(self):
        while True:
            self.__display_menu()
            self.__select_menu()

    def __input_student(self):
        name = input("请输入姓名：")
        age = int(input("请输入年龄："))
        score = int(input("请输入成绩："))
        stu = StudentModel(name, age, score)
        self.__manager.add_student(stu)

    def __output_students(self,list_output):
        for item in list_output:
            print(item.id,item.name,item.age,item.score)

    def __delete_student(self):
        id = int(input("请输入编号:"))
        if self.__manager.remove_student(id):
            print("成功")
        else:
            print("失败")

    def __modify_student(self):
        stu = StudentModel()
        stu.id = int(input("请输入需要修改的编号:"))
        stu.name = input("请输入需要修改的名字:")
        stu.score = int(input("请输入需要修改的得分:"))
        stu.age = int(input("请输入需要修改的年龄:"))
        # stu = StudentModel(name,age,score,id)
        if self.__manager.update_student(stu):
            print("修改成功")
        else:
            print("修改失败")




"""
manager = StudentManagerController()
s01 = StudentModel("zs", 24, 100)
s02 = StudentModel("ls", 24, 100)
manager.add_student(s01)
manager.add_student(s02)
for item in manager.stu_list:
    print(item.name,item.age,item.score,item.id)
"""

view = StudentManagerView()
view.main()






