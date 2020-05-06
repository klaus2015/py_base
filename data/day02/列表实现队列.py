
class QueueError(Exception):
    pass



class Queue:
    """
        列表尾进 头出
    """
    def __init__(self):
        self._queue = []
    # 查看是否空
    def is_empty(self):
        return self._queue == []

    # 入队
    def enqueue(self,val):
        self._queue.append(val)
    # 出队
    def dequeue(self):
        if self.is_empty():
            raise QueueError("空")
        return self._queue.pop(0)
    # 查看队顶
    # def top(self):
    #     if self.is_empty():
    #         raise QueueError("空")
    #     return self._queue[0]

if __name__ == "__main__":
    q = Queue()
    for i in range(10):
        q.enqueue(i)
    from 列表实现栈 import *
    st = SStack()
    while not q.is_empty():
        st.push(q.dequeue())

    while not st.is_empty():
        q.enqueue(st.pop())
    while not q.is_empty():
        print(q.dequeue())


