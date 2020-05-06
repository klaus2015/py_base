"""
    技能系统
"""


class SkillImpactEffect:
    """
        技能影响效果
    """

    def impact(self):
        raise NotImplementedError()

class DameageEffect(SkillImpactEffect):
    def __init__(self):
        self.value = value
    """
        伤害生命效果
    """
    def impact(self):
        print("扣你%d血" % self.value)

class LowerDeffenseEffect(SkillImpactEffect):



