from 数据结构.二叉树的序列化和反序列化 import Codec
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def treeToDoublyList(self, root: "Node") -> "Node":
        if not root:
            return
        pre:Node = None
        head:Node=None

        def treetopreandpost(root:Node):
            if not root:
                return
            if root.left:  #其实没必要可能
                treetopreandpost(root.left)
            nonlocal pre
            print(root.val)
            if pre!=None:
               root.left=pre

               pre.right=root
            else:
              nonlocal head
              head=root
            # root
            pre=root#用于保存顺序
            treetopreandpost(root.right)


        treetopreandpost(root)
        pre.right=head
        head.left=pre
        return head
if __name__ == '__main__':
    print(Solution().treeToDoublyList(Codec().deserialize([])))