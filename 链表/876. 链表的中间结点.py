
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution():
    def middleNode(self, head: ListNode) -> ListNode:
        if not head :
            return None

        slow=head
        fast=head
        while(fast.next):
            slow=slow.next
            fast=fast.next
            if fast.next:
                fast=fast.next

        return slow