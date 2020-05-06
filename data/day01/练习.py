# 　创建节点类
class Node:
    """
    思路：　将自定义的类视为节点的生成类，实例对象中
    　　　　包含数据部分和指向下一个节点的ｎｅｘｔ
    """

    def __init__(self, val, next=None):
        self.val = val  # 有用数据
        self.next = next  # 循环下一个节点关系

#　做链表操作
class LinkList:
    """
    思路：　单链表类，生成对象可以进行增删改查操作
    　　　　具体操作通过调用具体方法完成
    """
    def __init__(self):
        self.head = Node(None)

    # 通过list_为链表添加一组节点
    def init_list(self,list_):
        p = self.head
        for item in list_:
            p.next = Node(item)
            p = p.next

    # 遍历链表
    def show(self):
        p = self.head
        while p.next is not None:
            print(p.next.val)
            p = p.next

    # 判断链表为空
    def is_empty(self):
        p = self.head
        # if p.next is not None:
        #     return False
        # else:
        #     return True
        return False if p.next is not None else True

    # 清空链表
    def clear(self):
        self.head.next = None

    # 　尾部插入
    def append(self,val):
        p = self.head
        while p.next is not None:
            p = p.next
        p.next = Node(val)

    # 　头部插入
    def head_insert(self,val):
        # node = Node(val)
        # node.next = self.head.next
        # self.head.next = node
        self.head.next = Node(val,self.head.next)

    # 　指定插入位置
    def insert(self,index,val):
        p = self.head
        for i in range(index):
            if p.next is None:
                break
            p = p.next
        node = Node(val)
        node.next = p.next
        p.next = node

    # 　删除节点
    def delete(self,val):
        p = self.head
        while p.next and p.next.val != val:
            p = p.next

        if p.next is None:
            raise ValueError("不存在")
        else:
            p.next = p.next.next

    # 　获取某个节点值,传入节点位置获取节点值
    def get_index(self, index):
        p = self.head
        if index < 0:
            raise IndexError("index out of ")
        for i in range(index):
            if p.next is None:
                raise IndexError("index out of ")
            p = p.next
        print(p.val)

l1 = LinkList()
l1.init_list([1,2,3,6,9,13,21,25,28])
l2 = LinkList()
l2.init_list([4,5,7,8,10,11,12])

# 将l2合并到l1中
def merge(l1,l2):
    p = l1.head
    q = l2.head.next
    while p.next:
        if p.next.val < q.val:
            p = p.next
        else:
            temp = p.next
            p.next = q
            p = p.next
            q = temp
    p.next = q
merge(l1,l2)
l1.show()




















