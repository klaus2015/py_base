from  common.list_helper import *

class SkillData:
    def __init__(self,id,name,atk_ratio,duration):
        self.id = id
        self.name = name
        self.atk_ratio = atk_ratio
        self.duration = duration

    def __str__(self):
        return "技能:%d,%s,%d,%d" %(self.id,self.name,self.atk_ratio,self.duration)

list_skill = [
    SkillData(101,"乾坤大挪移",5,10),
    SkillData(102,"降龙十八掌",8,5),
    SkillData(103,"葵花宝典",10,2),
    ]



def condition01(item):
    return item.name == "葵花宝典"

def condition02(item):
    return item.id == 101

def condition03(item):
    return item.duration > 0

# re = ListHelper.find(list_skill,condition03)
# print(re)
re = ListHelper.find_count(list_skill,lambda item: len(item.name) >  4)
print(re)

re = ListHelper.find_count(list_skill,lambda item: item.duration < 5)
print(re)

re = ListHelper.find_count(list_skill,lambda item: item.duration>= 5)
print(re)

