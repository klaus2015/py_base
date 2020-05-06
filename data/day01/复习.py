"""
linklist.py
功能：　实现单链表的构建和功能操作
重点代码
"""
# 创建节点类
class Node:
    """
    初始化链表,标记一个链表的开端,以便于获取后端的节点
    """
    def __init__(self,val,next=None):
        self.val = val
        self.next = next


class LinkList:

    def __init__(self):
        self.head = Node(None)

    # 通过list_为链表添加一组节点
    def init_list(self, list_):
        p = self.head
        for item in list_:
            p.next = Node(item)
            p = p.next

    # 遍历链表
    def show(self):
        p = self.head.next
        while p is not None:
            print(p.val)
            p = p.next

    # 判断链表是否为空
    def is_empty(self):
        if self.head.next is None:
            return True
        else:
            return False

    def clear(self):
        self.head.next = None

    # 末尾插入
    def append(self,val):
        p = self.head
        while p.next is None:
            p = p.next
        p.next = Node(val)

    # 头部插入
    def head_insert(self,val):
        node = Node(val)
        node.next = self.head.next
        self.head.next = node

    # 指定位置插入
    def insert(self,index,val):
        p = self.head
        for i in range(index):
            if p.next is None:
                break
            p = p.next
        node = Node(val)
        node.next = p.next
        p.next = node

    # 删除
    def delete(self,x):
        p = self.head
        while p.next and p.next.val != x:
            p = p.next

        if p.next is None:
            raise ValueError('x is not in linklist')
        else:
            p.next = p.next.next

    # 获取某个节点的值
    def get_index(self,index):
        if index < 0:
            raise IndexError('index out of range')
        p = self.head.next
        for i in range(index):
            if p.next is None:
                raise IndexError('index out of range')
            p = p.next
        return p.val

l = LinkList()
l.init_list([1,2,3,4,5,6])
print(l.get_index(0))
l.append(7)
l.show()



