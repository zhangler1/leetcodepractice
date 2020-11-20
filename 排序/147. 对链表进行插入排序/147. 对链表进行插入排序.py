class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __repr__(self) -> str:
        return f" {self.val} ->{self.next.__repr__()}"

#记录几点关键点
# 用自己的链表模拟了，而且非常好玩，自己写了一个repr居然非常有用，很好玩！！！
# 插入节点的时候务必记录前驱节点，和后继节点
# 原链表中 从源节点断开 也要记录源后继节点
class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        header:ListNode=ListNode(-float("inf"))#header of orderLinkList

        p=head
        while(p!=None):
            tem=p.next
            loc=header
            pre=None
            while(loc!=None): #曾经写成loc。next！=None
                if loc.val<=p.val:
                    pre=loc
                    loc=loc.next
                else:
                    break
            if pre!=None:
                loc=pre
            post=loc.next
            loc.next=p
            p.next=post
            p=tem
        return header.next
from 链表.链表序列化与打印 import LinkList
if __name__ == '__main__':

    print(Solution().insertionSortList(LinkList([-1,5,3,4,0]).head))



