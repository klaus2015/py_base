'''给定一个只包括 '('，')'，'{'，'}'，'['，']' ，'<'，'>' 的字符串，判断字符串是否有效。 有效字符串需满足: 
左括号必须用相同类型的右括号闭合。 
左括号必须以正确的顺序闭合。 
注意空字符串可被认为是有效字符串。 
示例 1: 输入: "()" 输出: true 
示例 2: 输入: "()[]{}<>" 输出: true 
示例 3:输入: "(<{)]}" 输出: false 
示例 4: 输入: "([{ }]" 输出: false 
示例 5:输入: "(<{[()]}>)" 输出: true 
'''
class QueueError(Exception):
    pass

class Node:
    def __init__(self, val,next=None):
        self.val = val
        self.next = next

class LQueue:
    def __init__(self):
        self.front = self.rear = Node(None)

    def is_empty(self):
        return self.front == self.rear

    def enqueue(self, val):
        node = Node(val)
        self.rear.next = node
        self.rear = self.rear.next

    def dequeue(self):
        if self.front == self.rear:
            raise QueueError("Queue is empty")
        # 认为front指向的节点已经出队
        self.front = self.front.next
        return self.front.val


if __name__ == "__main__":
    sq = LQueue()
    lq = LQueue()
    lq.enqueue(10)
    lq.enqueue(20)
    lq.enqueue(30)
    print(lq.dequeue())
    print(lq.dequeue())
    print(lq.dequeue())




