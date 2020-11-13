class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:

        p=ListNode()
        head=p
        p1=l1
        p2=l2
        while(p1!=None and p2!=None):
            if p1.val>=p2.val:
                p.next=p2
                p2=p2.next
                p=p.next
            else:
                p.next=p1
                p1=p1.next
                p=p.next
        if p1==None:
            p.next=p2
        else:
            p.next=p1
        return head.next






        