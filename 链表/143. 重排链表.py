class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """

        def middleNode( head: ListNode) -> ListNode:
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

        def reverseLinkList(head:ListNode)->ListNode:
            if not head:
                return  None

            pre=None
            p=head
            while(p):
                tem=p.next
                p.next=pre
                pre=p
                p=tem
            return pre
        def mergeLinkList(list1:ListNode,list2:ListNode):
            if not list1 and not list2:
                return None

            head=ListNode()
            p=head
            l1=list1
            l2=list2
            while(l1 or l2):
                if l1:
                    p.next=l1
                    l1=l1.next
                    p=p.next

                if l2:
                    p.next=l2
                    l2=l2.next
                    p=p.next
            return head.next

        if not head:
            return []
        if not head.next:
            return head

        mid=middleNode(head)
        p=head
        while(p.next!=mid):
            p=p.next
        p.next=None


        secondlist=reverseLinkList(mid)

        mergeLinkList(head,secondlist)



