class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if not head :
            return None
        pre=head
        len=1
        while(pre):
            pre=pre.next
            len=len+1
        pre.next=head
        p=head
        for a in len-k%len :
            pre=pre.next
            p=p.next
        pre.next=None

        return p

