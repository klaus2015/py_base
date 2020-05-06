class StudentInfo:
    def input_value(self):
        pass

class AgeInfo(StudentInfo):
    def input_value(self):
        return input("请输入你的年龄")



class ScoreInfo(StudentInfo):
    def input_value(self):
        return input("请输入你的成绩")


class IdInfo(StudentInfo):
    def input_value(self):
        return input("请输入你的编号")



class StudentManagerView:

    def __init__(self):
        self.info = StudentInfo()


    def input_student(self):
        name = input("请输入学生姓名:")
        stu = []
        while True:

            str_value = self.info.input_value()
            try:
                value = int(str_value)
            except ValueError:
                print("请输入整数")
                continue
            if 10 <= value <= 20:
                stu.append(value)
            else:
                print("超出范围")
        return stu






ss = StudentInfo()
r= ss.input_value()
print(r)
