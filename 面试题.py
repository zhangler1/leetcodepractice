# 任意大小的字典，实现q，v交换
from random import randrange


def quciksort(l:list[int],left:int,right:int):
    if right-left<1:
        return


    def partition(l:list[int],left:int,right:int):
        rand=randrange(left,right+1)
        l[rand],l[left]= l[left], l[rand]
        pivot=l[left]
        i=left
        j=right
        while(j>i):
            while(l[j]>=pivot and j>i):
                j-=1
            l[i]=l[j]
            while(l[i]<=pivot and j>i):
                i+=1
            l[j]=l[i]
        l[i]=pivot
        return i


    mid=partition(l,left,right)
    quciksort(l,left,mid-1)
    quciksort(l,mid+1,right)

    return l




if __name__ == '__main__':
    a=   [9,2,2,5,6,10,15]
    print(quciksort(a,0,len(a)-1))