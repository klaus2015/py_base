"""
lstack.py  栈的链式栈
重点代码

思路分析：
1. 源于链表结构
2. 封装栈的操作方法（入栈，出栈，栈空，栈顶元素）
3. 链表的开头作为栈顶 ？ （不用每次遍历）
"""

# 自定义异常
class StackError(Exception):
    pass

# 节点类
class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next