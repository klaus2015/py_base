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