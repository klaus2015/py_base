# class A(object):
#     def go(self):
#         print("go A go")
# class B(A):
#     def go(self):
#         super().go()
#         print("go B go")
# class C(A):
#     def go(self):
#         super().go()
#         print("go C go")
# class D(B,C):
#     def go(self):
#         super().go()
#         print("go D go")
#
# d = D()
# print(D.mro())
# d.go()

# class Node(object):
#     def __init__(self,sName):
#         self.sName = sName
#         self._IChildren = []
#     def __repr__(self):
#         return "<Node {}>".format(self.sName)
#     def append(self,*args,**kwargs):
#         self._IChildren.append(*args,**kwargs)
#     def print_all_1(self):
#         print(self)
#         for oChild in self._IChildren:
#             oChild.print_all_1()
#
#     def print_all_2(self):
#         def gen(o):
#             IAll = [o,]
#             while IAll:
#                 oNext = IAll.pop(0)
#                 IAll.extend(oNext._IChildren)
#                 yield oNext
#         for oNode in gen(self):
#             print(oNode)
# oRoot = Node("root")
# childlist = []
# for i in range(1,11):
#     childlist.append(Node("child%s"%i))
#
# oRoot.append(childlist[0])
# oRoot.append(childlist[1])
# oRoot.append(childlist[2])
# childlist[0].append(childlist[3])
# childlist[0].append(childlist[4])
# childlist[1].append(childlist[5])
# childlist[3].append(childlist[6])
# childlist[2].append(childlist[7])
# childlist[2].append(childlist[8])
# childlist[5].append(childlist[9])
# oRoot.print_all_1()
# oRoot.print_all_2()
l = dict([(1,2),(3,4)])
print(l)
a = dict(((1,2),(3,4)))
print(a)


