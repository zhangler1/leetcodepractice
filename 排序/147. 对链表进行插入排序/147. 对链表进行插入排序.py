class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __repr__(self) -> str:
        return print(self.val,self.next.__repr__())


class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        header:ListNode=ListNode(-float("inf"))#header of orderLinkList

        p=head
        while(p!=None):
            tem=p.next
            loc=header
            pre=header
            while(loc.next!=None):
                if loc.val<=p.val:
                    pre=loc
                    loc=loc.next
                else:
                    break
            loc=pre
            post=loc.next
            loc.next=p
            p.next=post
            p=tem
        return header.next
from 链表.链表序列化与打印 import LinkList
if __name__ == '__main__':

    print(Solution().insertionSortList(LinkList([4,2,1,3]).head))



