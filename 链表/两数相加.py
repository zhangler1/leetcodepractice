from  typing import  List
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:

        head=ListNode(0)
        p1, p2,p3 = l1, l2,head
        carry=0
        while (not p1.next==None or not p2.next==None or not carry==0)    :

            carry,p3.val=divmod((p1.val+p2.val+carry),10)
            if (p1.next==None) :
                    p1.val=0
            else:
                p1=p1.next
            if (p1.next==None)  :
                    p2.val=0
            else:
                p2=p2.next
            p3.next=ListNode(0)

        return head


