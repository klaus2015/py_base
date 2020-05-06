"""
    参照day10/exercise02.py
    完成下列练习
"""
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
# 练习1:获取攻击比例大于6的所有技能
# 要求:使用生成器函数/生成器表达式完成
# def get_atk(list_target):
#     for item in list_target:
#         if item.atk_ratio > 6:
#             yield item
# for item in get_atk(list_skill):
#     print(item)

# re = (item.name for item in list_skill if item.atk_ratio > 6)
# for item in re:
#     print(item)

# def get_duration(list_target):
#     for item in list_target:
#         if 4 < item.duration < 11:
#             yield item
# for item in get_duration(list_skill):
#     print(item)
#
# re = (item for item in list_skill if 4<item.duration<11)
# for item in re:
#     print(item)
# 找出技能id是102的技能,仅此一个,直接用return就可以了

def get_duration(list_target):
    for item in list_target:
        if item.id == 102:
            return item
re = get_duration(list_skill)
print(re)
# def get_target(list_target):
#     for item in list_target:
#         if len(item.name) > 4 and item.duration < 6:
#             yield item
# for item in get_target(list_skill):
#     print(item)