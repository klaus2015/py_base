"""
bitree.py  二叉树的简单实践

思路分析：
1. 使用链式存储，一个Ｎｏｄｅ表示一个树的节点
2. 节点考虑使用两个属性变量分别表示左连接和右连接
"""

#　二叉树节点
class Node:
    def __init__(self,val,left=None,right = None):
        self.val = val
        self.left = left
        self.right = right

# 二叉树遍历类
class Bitree:
    def __init__(self,root = None):
        self.root = root

    #　先序遍历
    def preOrder(self,node):
        if node is None:  #　终止条件
            return
        print(node.val,end = '')
        self.preOrder(node.left)
        self.preOrder(node.right)

    # 　中序遍历
    def inOrder(self, node):
        if node is None:  # 终止条件
            return
        self.preOrder(node.left)
        print(node.val,end = "")
        self.preOrder(node.right)


if __name__ == "__main__":
    # B F G  D  I H E C A
    #　根据后续遍历构建二叉树
    b = Node('B')
    f = Node('F')
    g = Node('G')
    d = Node('D',f,g)
    i = Node('I')
    h = Node('H')
    e = Node('E',i,h)
    c = Node('C',d,e)
    a = Node('A',b,c)  #树根

    #　将a作为遍历的起始位置
    bt = Bitree(a)

    bt.preOrder(bt.root)
    print()
    bt.inOrder(bt.root)
