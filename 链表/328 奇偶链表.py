# 给定一个单链表，把所有的奇数节点和偶数节点分别排在一起。请注意，这里的奇数节点和偶数节点指的是节点编号的奇偶性，而不是节点的值的奇偶性。
#
# 请尝试使用原地算法完成。你的算法的空间复杂度应为 O(1)，时间复杂度应为 O(nodes)，nodes 为节点总数。
#
# 示例 1:
#
# 输入: 1->2->3->4->5->NULL
# 输出: 1->3->5->2->4->NULL
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        i=1
        p=head
        odd=ListNode()
        oddhead=odd
        even=ListNode()
        evenhead=even
        while(p!=None):

            if i%2==0:
              even.next=p
              even=even.next
            else:
                odd.next=p
                odd=odd.next
            p=p.next
            i+=1
        odd.next=None
        even.next=None
        pre=None

        for p in [oddhead.next,evenhead.next]:
            if pre!=None:
                pre.next=p
            while(p!=None):
                pre=p
                p=p.next
        return oddhead.next


