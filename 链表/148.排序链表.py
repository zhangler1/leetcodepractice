from 链表.链表序列化与打印 import ListNode,LinkList
class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        def merge(l1:ListNode,l2:ListNode):
            p=ListNode()
            head=p
            while(l1 and l2):
                if l1.val>l2.val:
                    p.next=l2
                    p=p.next
                    l2=l2.next
                else:
                    p.next=l1
                    p=p.next
                    l1=l1.next

            if l1:
                p.next=l1
            else:
                p.next=l2
            return head.next
        def mergeSort(head:ListNode):
            if  not head or not head.next:
                return  head

            fast=head
            l1=fast#第一段的开头

            slow=head
            while(fast.next):  ##若是多走一步就会坠入悬崖，那么这叫做稳妥写法
                if fast.next:
                    fast=fast.next
                if fast.next:
                    fast = fast.next
                if slow.next!=fast: #有明显分界线
                    slow=slow.next

            l2=slow.next#第二段的开头
            slow.next=None#关键 这样才能断开

            l1=mergeSort(l1)
            l2=mergeSort(l2)
            return merge(l1,l2)

        return mergeSort(head)
            

if __name__ == '__main__':
    print(Solution().sortList(LinkList([4, 2, 1, 3,23,3,4,2,1,5]).head))
