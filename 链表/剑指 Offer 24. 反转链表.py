
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
#这回记得返回pre 却忘记了 ，保存post
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if not head:
            return None
        pre=None
        p=head
        post=p.next

        while(p!=None):
            post=p.next
            p.next=pre
            pre=p
            p=post
        return pre

