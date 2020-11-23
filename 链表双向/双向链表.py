from typing import List, Iterator,Any


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


    def pop(self, __index: int = ...) ->Any :

        return

    def insert(self, __index: int, __object: Any) -> None:
        super().insert(__index, __object)

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

        print(DLinkedList([1,23,123]))




