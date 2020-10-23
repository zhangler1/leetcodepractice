class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        dummy=ListNode()
        dummy.next=head
        fast=dummy
        slow=dummy

        for i in range(n):
            fast=fast.next


        while fast.next :
            fast=fast.next
            slow=slow.next

        slow.next=slow.next.next
        return dummy.next




