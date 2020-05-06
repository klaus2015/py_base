"""
链表实现栈
"""

# 自定义异常类

class StackError(Exception):
    pass

class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


class LStack:
    def __init__(self):
        self.