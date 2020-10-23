from  typing import  List
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        p=head
        pre=head
        big=None
        small=None
        equal=None

        while(p) :
            p=p.next
            if(pre.val>x):
                pre.next=big
                big=pre
            if(pre.val==x):
                pre.next=equal
                equal=pre
            if (small.val<x):
                pre.next=small
                small=pre
            pre=p
        cur=ListNode()
        head=cur
        for p in [small,equal,big]:
            cur.next=p
            while(p):
                p=p.next
                cur=cur.next
        return head.next


