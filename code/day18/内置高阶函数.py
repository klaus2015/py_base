class Enemy:
    def __init__(self, name, hp, atk, defense):
        self.name = name
        self.hp = hp
        self.atk = atk
        self.defense = defense

    def __str__(self):
        return "%s--%d--%d--%d" % (self.name, self.hp, self.atk, self.defense)


list01 = [
    Enemy("玄冥二老", 50, 120, 4),
    Enemy("成昆", 40, 70, 5),
    Enemy("谢逊", 80, 85, 6),
    Enemy("灭霸", 100, 100, 10),
    ]
tuple01 = ([1,1,1],[2,2],[3,3,3,3])
re = max(tuple01,key=lambda item: len(item))
print(re)
print("--------------")
# re = map(lambda item:(item.name,item.hp,item.atk),list01)
# for item in re:
#     print(item)
# print("--------------")
# re = filter(lambda item:item.atk>100 and item.hp > 0,list01)
# for item in re:
#     print(item)
#
# print("--------------")
# re = sorted(list01,key=lambda item:item.defense,reverse=True)
# for item in re:
#     print(item)
#
# list02 = [1,59,60,100,4,27]
# re = sorted(list02,key=lambda item:item > 20)
# print(re)