class ListNode:
 def __init__(self,val=0,next=None):
     self.val=val
     self.next=next

 def __repr__(self) -> str:
     return str(self.val)+self.next.__repr__()
    #None的repr是“None”
from  typing import  List
class LinkList:
    def __init__(self,list:List):
        self.head=None
        pre=None
        for item in list:

            p = ListNode(item)
            if not self.head:
                self.head=p
            if pre:
                pre.next=p
            pre=p



