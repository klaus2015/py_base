# def print_rectangle(row_count, column_count,char):
#     """
#     打印多行*
#
#     """
#     for r in range(row_count): # 外层循环控制行
#         for c in range(column_count): # 内层循环控制列
#             print(char, end = " ")
#         print()
#
# print_rectangle(3, 4,"*")
# print_rectangle(4, 5,"#")


def print_list(list_target):
    """
    打印列表，每行一个元素
    :param list_target: 目标列表
    :return:
    """

    for i in list01:
        print(i)
list01 = [1,2,3]
print_list(list01)