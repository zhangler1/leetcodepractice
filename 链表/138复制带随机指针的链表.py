class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        #将原链表的索引，地址对应好
        p=head
        ptoindex=dict()
        pnewtoindex=dict()
        i=0


        pnew=Node(0)#值在这个节点，链接却需要上个节点
        headnew=pnew


        indextop=[]
        while(p!=None):  #复制值，并得到2个索引，地址映射表
            pnew.next=Node(p.val)
            pnew=pnew.next

            pnewtoindex[pnew]=i
            ptoindex[p]=i
            indextop.append(pnew)
            i+=1
            p=p.next

        p=head#为了得到random索引映射表
        #index to index
        random={}
        while(p!=None):
            if p.random!=None:
                random.update({ptoindex[p]: ptoindex[p.random]})
            p=p.next
        #得到了重建的元素



        headnew=headnew.next
        pnew=headnew
        i=0
        while pnew!=None:
            if random.get(i,None)!=None:
                pnew.random=indextop[random.get(i,None)]
            else :
                pnew.random=None
            pnew=pnew.next
            i+=1
        return   headnew
