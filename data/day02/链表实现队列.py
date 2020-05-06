
class QueueError(Exception):
    pass


class Node:
    def __init__(self, val, next=None):
        self.val = val  # 有用数据
        self.next = next  # 循环下一个节点关系

class LQueue:
    def __init__(self):
        self.front = self.rear = Node(None)

    def is_empty(self):
        return self.front == self.rear

    def enqueue(self,val):
        node = Node(val)
        self.rear.next = node
        self.rear = node
        # self.rear.next = Node(val)
        # self.rear = node

    def dequeue(self):
        if self.front == self.rear:
            raise QueueError
        self.front = self.front.next
        return self.front.val
if __name__ == "__main__":
    l = LQueue()
    l.enqueue(1)
    l.enqueue(2)
    l.enqueue(3)
    print(l.dequeue())
    print(l.dequeue())
    