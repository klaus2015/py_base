
def rank_list(list_target):
    for r in range(len(list_target) - 1):

        for c in range(r + 1, len(list_target)):

            if list_target[r] > list_target[c]:
                list_target[r], list_target[c] = list_target[c], list_target[r]   # 修改的传入的对象，即list01，
                                                                                    # 后面不需要retur返回修改后的结果



list01 = [3, 80, 45, 5, 7, 1]
rank_list(list01)
print(list01)

