from functools import reduce
from typing import Iterable
from typing import Any



def GreatestCommonDivisor(first:int,second:int):
    a=max(first,second)
    b=min(first,second)
    if b==0:
        return a
    else:
        return GreatestCommonDivisor(b,a%b)
def GreatestCommonDivisorofiter(iter:Iterable[Any]):
    nums=list(iter)
    print(iter.__class__)
    return  reduce(GreatestCommonDivisor,nums)

#最大公约数可以理解为质因数之积，所以多个数的最大公约数要依次最大质因数

if __name__ == '__main__':
    print(GreatestCommonDivisorofiter([-1,-10]))