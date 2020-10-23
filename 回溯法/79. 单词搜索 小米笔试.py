board=[["C","A","A"],["A","A","A"],["B","C","D"]]
word="AAB"



from typing import  List
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        path=[]
        for l in range(len(board[0])):
            for w in range(len(board)):
                if board[w][l]==word[0]:
                    path.append((w,l)) #曾经不小心挡住了
                    if dfs(board,word,path,(w,l),0):
                        return True
                    path.pop()


        return  False


def dfs(board:List[List[str]],word:str,path:List[int],selection:(int,int),hierachy=0)-> bool:
       if len(word)<hierachy:
           return  False

       if hierachy==len(word)-1:
           return True

       result=False

       for step in (0,1),(1,0),(-1,0),(0,-1):
           trya=(selection[0]+step[0],selection[1]+step[1])
           if 0<=trya[0]<len(board )and   0<=trya[1]<len(board[0]):
               if trya not in path:#因为误以为挡住了
                   path.append(trya)
                   if board[trya[0]][trya[1]] == word[hierachy+1] :
                        result=result or dfs(board,word,path,trya,hierachy+1)
                   path.pop()
       return result





print(Solution().exist(board=board, word=word))