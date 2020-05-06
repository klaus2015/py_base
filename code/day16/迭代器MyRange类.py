class MyRange:
    def __init__(self, value):
        self.value = value

    def __iter__(self):
        return NumIterator(self.value)


class NumIterator:
    def __init__(self,target):
        self.target = target
        self.index = 0

    def __next__(self):
        if self.index == self.target:
            raise StopIteration
        temp = self.index
        self.index += 1
        return temp




#
# my = MyRange(10)

for item in MyRange(10):
    print(item)





# for item in myrange(10):


# iterator = my.__iter__()
#
# while True:
#     try:
#         item = iterator.__next__()
#         print(item)
#     except StopIteration:
#         break