
class ListNode:
 def __init__(self,val=0,next=None):
     self.val=val
     self.next=next

class Solution :
      def sortList(self,head:ListNode) -> ListNode:
        if (head == None or head.next == None):
            return head;
        fast = head.next #快慢指针
        slow = head
        while (fast != None and fast.next != None) :
            slow = slow.next;
            fast = fast.next.next;
        mid = slow.next;    #获得中点并且
        slow.next = None;  #断开
        left = self.sortList(head);  #左边归并结束
        right = self.sortList(mid);  #右边归并结束
        mergep =  ListNode(0);  #合并用指针。穿针引线
        mergeh = mergep; #合并的头结点，也可以使用头插法，不用头结点
        while (left != None and right != None):
            if (left.val < right.val) :
                mergep.next = left;
                left = left.next;
            else:
                mergep.next = right;
                right = right.next;

            mergep = mergep.next;

        mergep.next = left if (left != None ) else right;
        return mergeh.next
      def quickList(self,head:ListNode)->ListNode:
          if (not head or not head.next):
              return head
          biger = None
          equal = None
          small = None
          p = head
          while (p):
              tem = p
              p = p.next     #注意前插法的使用保留 ，前进
              if (tem.val > head.val):
                  tem.next = biger
                  biger = tem       #前插法
              if (tem.val < head.val):
                  tem.next = small
                  small = tem
              if tem.val == head.val:
                  tem.next = equal
                  equal = tem

          biger = self.sortList(biger)   #返回值记得要保留 因为 需要两列表头指针
          small = self.sortList(small)

          head = t = ListNode()
          for p in [small, equal, biger]:  #链接3表  跟随法，p跨越时代 ，t 保留到最后一个，以防成为断链  ，pt同步推进
              while p:
                  t.next = p
                  p = p.next
                  t = t.next
          return head.next


          







          

          




