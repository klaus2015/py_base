class Vector1:
    def __init__(self,x):
        self.x = x

    def __str__(self):
        return "一维向量的分量是:" + str(self.x)

    # def __sub__(self, other):
    #     return Vector1(self.x - other)
    #
    # def __mul__(self, other):
    #     return Vector1(self.x * other)

    def __rsub__(self, other):
        return Vector1(self.x - other)


    def __rmul__(self, other):
        return Vector1(self.x * other)


v01 = Vector1(10)
# print(v01 - 5)
# print(v01 * 5)
print(5-v01)
print(5*v01)