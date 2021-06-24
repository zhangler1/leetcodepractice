from typing import List
class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        purse5=0
        purse10=0
        ans=[]
        for bill in bills:
            if bill==5:
                purse5+=1
                ans.append(f"收5块 5:{purse5} 10:{purse10}")
            if bill==10:
                if purse5>0:

                    purse5-=1
                    purse10+=1
                    ans.append(f"收10块，找5块 5:{purse5} 10:{purse10}")
                else:
                    return False
            if bill==20:
                if purse10>0 and purse5>0:
                    purse5-=1
                    purse10-=1
                    ans.append(f"收20块，找10+5块  5:{purse5} 10:{purse10}")
                elif purse5>=3:
                    purse5-=3
                    ans.append(f"收20块，找3*5块  5:{purse5} 10:{purse10}")
                else:
                    return False
        # print(ans)
        return True
if __name__ == '__main__':
    print(Solution().lemonadeChange([5, 5, 5, 10, 20]))
