from typing import List, Iterator,Any ,overload


class ListNode():
    def __init__(self,val=None) -> None:
        self.val=val
        self.next=None
        self.pre=None



    def __repr__(self) -> str:

        return f"{self.val}"
class DummyNode(ListNode):

    def __repr__(self) -> str:
        return "header"


class DLinkedList(Iterator,List):
    #有多少变量是需要整个类共有的？？整个类一共实例化多少实例？？
    @overload
    def pop(self):
        pass

    def pop(self, __index: int =...) ->Any :
        '''

        :param __index:
        :type __index:
        :return: 
        :rtype:
        '''
        if __index==...:
            if  self.head.next==self.head:
                raise IndexError("从空链表里弹出")
            p=self.head
            pre:ListNode=self.head
            while(pre==self.head or p!=self.head):
                pre=p
                p=p.next
            pre.pre.next=p #
            p.pre=pre.pre
            return pre.val
        if  self.head.next==self.head:
            raise IndexError("从空链表里弹出")
        else:
            i=0
            p=self.head
            pre=self.head
            while(i<=__index):
                pre=p
                p=p.next
                i+=1
            pre.next=p.next #
            pre.next.pre=pre
            p.next=None
            p.pre=None
            return p.val

    def insert(self, __index: int, __object: Any) -> None:
        '''

        asdfasdf
        Args:
            __index (int):
            __object (int):

        Returns: asdfasdf
        '''
        p=self.head
        pre=self.head   #通常附加条件,即可避免终止情况和初始情况相同的情况
        i=0
        while(i<=__index ):
            pre=p
            p=p.next
            i+=1

        pre.next=ListNode(__object)
        pre.next.pre=pre
        pre.next.next=p
        p.pre=pre.next




    def __iter__(self) :
        self.p=self.head.next #返回一个可初始化的函数，次函数返回一个迭代器
        return self

    def __next__(self): #迭代器需要记录状态的，因为你for 只是会一次次调用next（）而已，不会使用next的结果作为下一步的开始。
        if isinstance(self.p, DummyNode):
            raise StopIteration
        else:
            k=self.p
            self.p = self.p.next
            return k

    def __repr__(self) -> str:
        return  "<->".join([node.__repr__() for node in self]) #因为self本身就是一个实例，实现了iter（）方法


    def __init__(self,list:List[int]) -> None:
         self.head:DummyNode=DummyNode()
         p: ListNode = self.head#用作记录迭代进程

         pre:ListNode=self.head
         for item in list:
             node=ListNode(item)
             if  pre:
                 pre.next=node
                 node.pre=pre
             pre=node
         pre.next=self.head
         self.head.pre=pre
if __name__ == '__main__':
        d=DLinkedList([1, 23, 123])
        print(d.pop(0))
        print(d)
        print(d.insert(2,6))
        print(d)
        print(d.pop())
        print(d.pop())
        print(d.pop())

        print(d)




