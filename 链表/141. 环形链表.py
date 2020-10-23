# 141.
# 环形链表
# 给定一个链表，判断链表中是否有环。
from typing import List
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        if(not head):
            return False
        fast=head
        slow=head

        while(not fast.next==None):
            fast=fast.next.next
            slow=slow.next
            if(fast==slow):
                return True
        return False