
def judge_list_element(list_target):
    """

    :param list_target:
    :return:
    """


    for r in range(0, len(list_target) - 1):
        for c in range(r + 1, len(list_target)):
            if list_target[r] == list_target[c]:
                return True   # 有重复
    return False  # 没有重复

list01 = [3, 80, 31, 50, 81, 5]
print(judge_list_element(list01))