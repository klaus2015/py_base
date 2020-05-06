"""
    ２０４８　游戏核心算法
    16:50
"""

list_merge = None


# 练习１：零元素移至末尾
# 　　[2,0,2,0]  --> [2,2,0,0]
#    [2,0,0,2]  --> [2,2,0,0]
#    [2,4,0,2]  --> [2,4,2,0]

def zero_to_end():
    """
        零元素移动到末尾.
    """

    # 思想：从后向前，如果发现零元素，删除并追加.
    for i in range(-1, -len(list_merge) - 1, -1):
        if list_merge[i] == 0:
            del list_merge[i]
            list_merge.append(0)


# 测试．．．
# zero_to_end()
# print(list_merge)


# 练习2：将相同数字合并 14:38
# 　　[2,2,0,0]  --> [4,0,0,0]
#    [2,0,0,2]  --> [4,0,0,0]
#    [2,0,4,0]  --> [2,4,0,0]
#    [2,2,2,2]  --> [4,4,0,0]
#    [2,2,2,0]  --> [4,2,0,0]
def merge():
    """
        合并
    """
    # 先将中间的零元素移到末尾
    # 再合并相邻相同元素
    zero_to_end()

    for i in range(len(list_merge) - 1):
        if list_merge[i] == list_merge[i + 1]:
            # 将后一个累加前一个之上
            list_merge[i] += list_merge[i + 1]
            del list_merge[i + 1]
            list_merge.append(0)


# 测试...
# merge()
# print(list_merge)

# 练习3:地图向左移动
map = [
    [2, 0, 0, 2],
    [4, 4, 2, 2],
    [2, 4, 0, 4],
    [0, 0, 2, 2],
]


def move_left():
    """
        向左移动
    """
    # 思想:将二维列表中每行交给merge函数进行操作
    for line in map:
        global list_merge
        list_merge = line
        merge()


# move_left()
# print(map)

def move_right():
    """
        向右移动
    """
    # 思想:将二维列表中每行(从右向左)交给merge函数进行操作
    for line in map:
        global list_merge
        # 从右向左取出数据　形成　新列表
        list_merge = line[::-1]
        merge()
        # 从右向左接受　合并后的数据　
        line[::-1] = list_merge


# move_right()
# print(map)

# 练习4:向上移动　　向下移动
def move_up():
    square_matrix_transpose(map)
    move_left()
    square_matrix_transpose(map)


def move_down():
    square_matrix_transpose(map)
    move_right()
    square_matrix_transpose(map)


# 提示:利用方阵转置函数
def square_matrix_transpose(sqr_matrix):
    """
        方阵转置
    :param sqr_matrix: 二维列表类型的方阵
    """
    for c in range(1, len(sqr_matrix)):
        for r in range(c, len(sqr_matrix)):
            sqr_matrix[r][c - 1], sqr_matrix[c - 1][r] = sqr_matrix[c - 1][r], sqr_matrix[r][c - 1]


move_down()
print(map)
