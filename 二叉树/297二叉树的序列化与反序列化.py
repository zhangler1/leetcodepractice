# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
from collections import deque
class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        if not root:      #判断是否为空的树
            return []
        q= deque()
        q.append(root)
        serial=[]
        while(len(q)!=0):    #只要队列不为空
            node=q.popleft()
            if node:   #虽然都要加但是一个加node。val 另一个家None
                #秉承着，自己做自己的事的观点，如果放入子节点就帮孩子考虑好，那么需要考虑孩子的值了。个人认为这种做法没有必要
                serial.append(node.val)
                q.append(node.left)
                q.append(node.right)
            else:
                serial.append(None)
        while(serial[-1]==None):  #关键 去除最后的none
            serial.pop()
        


        return serial
    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        #将完整的元素入栈即可。
        if not data:
            return
        dque=deque(data)
        sque=deque()
        root=TreeNode(dque.popleft())
        sque.append(root)
        while len(sque)!=0:
            node=sque.popleft()
            if len(dque)!=0 :
                val=dque.popleft()   #  这里出现了失误每一次都需要判断的，否则会出现问题
                if val!=None:
                    node.left=TreeNode(val)
                    sque.append(node.left)
            if len(dque) != 0:
                val=dque.popleft()  #  这里出现了失误每一次都需要判断的，否则会出现问题
                if val!=None:
                    node.right=TreeNode(val)
                    sque.append(node.right)

        return root




# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
if __name__ == '__main__':
    print(Codec().serialize(Codec().deserialize(
        [1,2,3,None,None,4,5])))