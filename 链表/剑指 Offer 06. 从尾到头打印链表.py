from typing import List,Callable,Any,NoReturn
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def reverseLinkList(head:ListNode)->ListNode:
    p=head
    pre=None
    while(p!=None):
        tem=p.next
        p.next=pre
        pre=p
        p=tem

    return pre

def traverse(head:ListNode,option:Callable[[Any],Any]=lambda x:x):
    p=head
    ans=[]
    while(p!=None):

        ans.append(option(p.val))
        p=p.next
    return ans


class Solution:
    def reversePrint(self, head: ListNode) -> List[int]:
        head=reverseLinkList(head)


        tem=traverse(head)
        head=reverseLinkList(head)
        return tem
