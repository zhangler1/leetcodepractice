# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        def judgek(head:ListNode,int:k)->bool:
            if not head:
                return False

            p=head
            for a in range(k-1):
                if p.next:
                    p=p.next
                else:
                    return False
            return True

        def windowReverse(head:ListNode,windowlenth:int)->(ListNode,ListNode):
            if judgek(head,windowlenth):
                pre=None
                tail=head
                p=head
                for a in range(windowlenth):
                    temp=p.next
                    p.next=pre
                    pre=p
                    p=temp
                head=pre
                tail.next=temp
                return head,tail
            else:
                p=head
                while(p):
                    p=p.next
                return head,p

        head,tail=windowReverse(head,k)
        if tail:
            tail.next=self.reverseKGroup(tail.next,k)
        return head




from 链表.链表序列化 import LinkList

print(Solution().reverseKGroup(LinkList([1,2,3,4,5]).head,2))





