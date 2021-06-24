from 数据结构.二叉树的序列化和反序列化 import Codec
import heapq
class HuffmanTreeNode:
    def __init__(self, x):
        self.val = x
        self.left:HuffmanTreeNode = None
        self.right:HuffmanTreeNode = None

    def __lt__(self, other):
            return self.val<other.val
    def __add__(self, other):
        node=HuffmanTreeNode(self.val+other.val)
        node.left=self
        node.right=other
        return   node


class Solution:
    def HuffmanTree(self,elements:list[any]):
        Nodes=[ HuffmanTreeNode(a) for a in elements]
        heapq.heapify(Nodes)
        while(len(Nodes)>1):
            A=heapq.heappop(Nodes)
            B=heapq.heappop(Nodes)
            heapq.heappush(Nodes,A+B)

        return Codec().serialize(Nodes[0])
if __name__ == '__main__':
    print(Solution().HuffmanTree([3,4,10,8,6,5]))