class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        head=ListNode()
        p=head

        while(l1!=None and  l2!=None):
            if(l1.val<=l2.val):
                p.next=l1
                l1=l1.next
                p=p.next
            else:
                p.next=l2
                l2=l2.next
                p=p.next

        if (l1):
            p.next=l1
        else:
            p.next=l2
        return head.next