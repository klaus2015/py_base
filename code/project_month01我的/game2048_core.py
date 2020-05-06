"""
    2048游戏核心算法
"""
# 1.[2,0,2,0]  ---> [2,2,0,0]
# 1.[2,0,0,2]  ---> [2,2,0,0]
# 1.[2,4,0,2]  ---> [2,4,2,0]
list_merge = [4,4,0,2]
def zero_to_end():
    for i in range(-1,-len(list_merge)-1,-1):
        if list_merge[i] == 0:
            del list_merge[i]
            list_merge.append(0)
# zero_to_end()
# print(list_merge)
# 相同数字合并
# [2,2,0,0] -->[4,0,0,0]
#[2,2,2,2] --->[4,4,0,0]
#[2,2,2,0] --->[4,2,0,0]

def merge():
    zero_to_end()
    for i in range(len(list_merge)-1):
        if list_merge[i] == list_merge[i+1]:
            #将后一个累加前一个,再删掉,末尾加0
            list_merge[i] += list_merge[i+1]
            del list_merge[i+1]
            list_merge.append(0)

# merge()
# print(list_merge)

# 练习3
map = [
    [2,0,0,2],
    [4,4,2,2],
    [2,4,2,0],
    [0,0,2,2]
]
def move_left():
    for line in map:
        global  list_merge
        list_merge = line
        merge()
# move_left()
# print(map)

def move_right():
    for line in map:
        # 从右想左取出数据 形成新列表
        global  list_merge
        list_merge = line[::-1]

        merge()
        # 从右向左接受 合并后的数据
        line[::-1] = list_merge
# move_right()
# print(map)

# 向上移动
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

move_up()
for item in map:
    print(item)
