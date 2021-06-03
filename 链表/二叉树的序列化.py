# Definition for a binary tree node.
from collections import  deque
class TreeNode(object):
    def __init__(self,x):
        self.val = x
        self.left = None
        self.right = None

    def __repr__(self) -> str:
            return f"<-{str(self.val)}->"

class Codec:
    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        nodes=deque()
        nodes.append(root)
        serial=[]
        while(len(nodes)!=0):
            curnode=nodes.popleft()
            serial.append(curnode.val)
            if curnode.left:
                nodes.append(curnode.left)
            if curnode.right:
                nodes.append(curnode.right)

        while serial[-1]==0:
            serial.pop()
        return serial


    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        if len(data)==0:
            return None
        root=TreeNode(0)
        d=deque()
        d.append(root)
        nodevals=deque(data)

        while(len(nodevals)!=0):
            curnode:TreeNode=d.popleft()
            curnode.val=nodevals.popleft()
            if curnode.val:
                curnode.left=TreeNode(0)
                d.append(curnode.left)
                curnode.right=TreeNode(0)
                d.append(curnode.right)
        return root




if __name__ == '__main__':
    print(Codec().serialize(Codec().deserialize([1,2,3,None,None,4,5])))
# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))