class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        def middleNode(head:ListNode)->ListNode:
            if not head:
                return None

            slow=head
            fast=head
            while(fast.next):
                pre=slow
                slow=slow.next
                fast=fast.next
                if fast.next:
                    fast=fast.next
            pre.next=None
            return slow
        def reverseLinkListtil(head:ListNode,til:ListNode=None)->ListNode:
            p=head
            pre=None
            while(p!=til):
                tem=p.next
                p.next=pre
                pre=p
                p=tem
            return pre
        mid=middleNode(head)
        rightpartlinklist=reverseLinkListtil(mid,None)
        p=head
        m=rightpartlinklist
        while(p):
            if p.val==m.val:
                p=p.next
                m=m.next
            else:
                return False
        return True
            






