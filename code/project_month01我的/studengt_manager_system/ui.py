from project_month01.studengt_manager_system.model import StudentModel
from project_month01.studengt_manager_system.bll import StudentManagerController

class StudentManagerView:

    def __init__(self):
        self.__manager = StudentManagerController()


    def __display_menu(self):
        print("1)添加学生")
        print("2)显示学生")
        print("3)删除学生")
        print("4)修改学生")
        print("5)按照成绩升序显示学生")

    def __select_menu_item(self):

        item = input("请输入: ")

        if item == "1":
            self.__input_student()
        elif item == "2":
            self.__output_students(self.__manager.stu_list)
        elif item == "3":
            self.__delete_student()
        elif item == "4":
            self.__modify_student()
        elif item== "5":
            self.__output_student_by_score()

    def main(self):
        while True:
            self.__display_menu()
            self.__select_menu_item()

    def __input_student(self):
        name = input("请输入学生姓名:")
        age = self.input_value("请输入年龄:")
        score = self.input_value("请输入成绩:")
        stu = StudentModel(name,age,score)
        self.__manager.add_student(stu)

    def __output_students(self,list_output):
        for item in list_output:
            print(item.id,item.name,item.age,item.score)

    def __delete_student(self):
        id = int(input("请输入编号: "))
        self.__manager.remove_student(id)

    def __modify_student(self):
        id = self.input_value("请输入id")
        name = input("请输入学生姓名:")
        age = self.input_value("请输入修改的年龄")
        score = self.input_value("请输入修改的成绩")
        stu = StudentModel(name, age, score,id)
        self.__manager.update_student(stu)

    def __output_student_by_score(self):
        """
        根据成绩升序显示学生
        :return:
        """
        self.__manager.order_by_score()
        self.__output_students(self.__manager.stu_list)

    def input_value(self,message):

        while True:
            try:
                number = int(input(message))
                break
            except ValueError:
                print("出入错误")





