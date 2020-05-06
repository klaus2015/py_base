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