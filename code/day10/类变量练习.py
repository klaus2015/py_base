class Wife:
    """
        老婆类
    """
    count = 0
    @classmethod
    def print_count(cls):
        print("总共生产了%d个老婆类" % Wife.count)


    def __init__(self,name):
        self.name = name
        Wife.count += 1


wife01 = Wife("王昭君")
wife02 = Wife("甄姬")
wife03 = Wife("大乔")
Wife.print_count()

