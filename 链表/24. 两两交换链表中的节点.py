
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        p=head
        while p:
            if p.next:
                temp=p.next
                p.next=p.next.next
                temp.next=p
                p=p.next
        return head
