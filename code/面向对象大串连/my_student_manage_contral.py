class StudentModel:
    """
        学生数据类型
    """
    def __init__(self, name="", age=0, score=0, id=0):
        """

        :param name:姓名 str类型
        :param age: 年龄 int类型
        :param score: 分数 int类型
        :param id: 学生编号(该学生对象的唯一标识) int 类型
        """
        self.name = name
        self.age = age
        self.score = score
        self.id = id

class StudentManagerController:
    """
        学生管理控制器,负责学生逻辑处理
    """
    # 类变量,标识初始编号
    __init_id = 1000
    def __init__(self):
        self.__stu_list = []

    @property
    def stu_list(self):
        return self.__stu_list

    def add_student(self,stu_info):
        """

        :param stu_info: 添加的学生

        """
        StudentManagerController.__init_id += 1
        stu_info.id = StudentManagerController.__init_id
        self.__stu_list.append(stu_info)

    def remove_student(self,id):
        """

        :param id: 根据编号删除学生
        :return:True 标识删除成功; False 标识失败
        """
        for item in self.__stu_list:
            if item.id == id:
                self.__stu_list.remove(item)
                return True
            return False

    def update_student(self,stu_info):
        for item in self.__stu_list:
            if item.id == stu_info.id:
                item.name = stu_info.name
                item.age = stu_info.age
                item.score = stu_info.score
                return  True
            return False

    def order_by_score(self):
        """
            根据成绩对__stu_list进行排序
        :return: 无
        """
        for r in range(len(self.__stu_list)-1):
            for c in range(r+1,len(self.__stu_list)):
                if self.__stu_list[r].score > self.__stu_list[c].score:
                    self.__stu_list[r],self.__stu_list[c] = self.__stu_list[c],self.__stu_list[r]


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
        elif item == "5":
            self.__output_student_by_score()

    def main(self):
        while True:
            self.__display_menu()
            self.__select_menu_item()

    def __input_student(self):
        name = input("请输入学生姓名:")
        age = int(input("请输入学生年龄:"))
        score = int(input("请输入学生成绩: "))
        stu = StudentModel(name,age,score)
        self.__manager.add_student(stu)

    def __output_students(self,list_output):
        for item in list_output:
            print(item.id,item.name,item.age,item.score)

    def __delete_student(self):
        id = int(input("请输入编号: "))
        self.__manager.remove_student(id)

    def __modify_student(self):
        id = int(input("请输入学生编号: "))
        name = input("请输入学生姓名:")
        age = int(input("请输入学生年龄:"))
        score = int(input("请输入学生成绩: "))
        stu = StudentModel(name, age, score,id)
        self.__manager.update_student(stu)

    def __output_student_by_score(self):
        """
        根据成绩升序显示学生
        :return:
        """
        self.__manager.order_by_score()
        self.__output_students(self.__manager.stu_list)


view = StudentManagerView()
view.main()

