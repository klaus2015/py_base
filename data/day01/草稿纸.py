
from linklist import *
def merge(l1,l2):
    p = l1.head
    q = l2.head.next
    while p.next is not None:
        if p.next.val < q.val:
            p = p.next
        else:
            tem = p.next
            p.next = q
            p = p.next
            q = tem
    p.next = q





l1 = LinkList()
l2 = LinkList()
l1.init_list([1,2,3,4])
l2.init_list([5,6,7])
