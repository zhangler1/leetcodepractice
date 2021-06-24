from 数据结构.二叉树的序列化和反序列化 import Codec,TreeNode
class Solution:
    def countNodes(self, root: TreeNode) -> int:
        if not root:
            return 0
        deepth=0
        p=root
        while(p!=None):
            p=p.left
            deepth+=1
        #得到了深度
        #现在来深度优先寻找最末梢节点
        def dfs(root:TreeNode,Path=[],hierachy=1,ans=[]):
            if ans:#截断口，我只需要一个答案
                return 
            if not root:  #平凡退出口
                return
            if hierachy==deepth:
                ans.append(Path.copy())
            Path.append("right")
            dfs(root.right,Path,hierachy+1,ans)
            Path.pop()
            Path.append("left")
            dfs(root.left,Path,hierachy+1,ans)
            Path.pop()
        path=[]
        ans=[]
        dfs(root,path,ans=ans)
        i=0
        for routiue in ans[0]:
            if routiue=="left":
                i=2*i+1
            if routiue=="right":
                i=2*i+2
        return i+1

if __name__ == '__main__':
    print(Solution().countNodes(Codec().deserialize([1,2,3,4,5,6])))