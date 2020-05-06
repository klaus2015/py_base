"""[
    [1,2,3,44],
    [4,5,5,5,65,6,87],
    [7,5]
]
"""

def print_list(target_list):
    """
    打印二位列表
    :return:
    """
    for r in range(len(target_list)):
        for c in list01[r]:
            print(c, end = " ")
        print()

list01 = [
    [1,2,3,44],
    [4,5,5,5,65,6,87],
    [7,5]
]
print_list(list01)