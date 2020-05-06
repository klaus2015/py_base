class StackError(Exception):
    pass


class Node:
    def __init__(self, val, next=None):
        self.val = val  # 有用数据
        self.next = next  # 循环下一个节点关系

class Stack:
    def __init__(self):
        self._top = None

    def is_empty(self):
        if self._top is None:
            raise StackError

    def push(self,val):
        # self.top = Node(val,self.top) 一行搞定
        node = Node(val)
        node.next = self._top
        self._top = node

    def pop(self):
        if self._top is None:
            raise StackError
        value = self._top.val
        self._top =self._top.next
        return value

    def top(self):
        if self._top is None:
            raise StackError
        return self._top.val

if __name__ == "__main__":
    ls = Stack()
    ls.push(1)
    ls.push(2)
    ls.push(3)
    print(ls.pop())
    print(ls.pop())
    print(ls.top())

