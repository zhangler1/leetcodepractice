#本题线下没法模拟，因为是个带环的链表
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        fast=head
        slow=head
        p=head
        while(fast.next != None and fast.next.next!=None):
            fast=fast.next.next
            slow=slow.next
            if fast==slow:
                while (p != slow):
                    p = p.next
                    slow = slow.next
                return p
                #while循环的双出口却不保持结果的统一性





        return None






