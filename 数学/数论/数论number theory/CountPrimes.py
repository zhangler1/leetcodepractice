class Solution:
    def countPrimes(self, n: int) -> int:

        if n<=2:
            return 0
        isPrime=[1]*n
        isPrime[0],isPrime[1]=0,0
        Primes=[]
        for x in range(2,n):
            if isPrime[x]==1:
                Primes.append(x)
                k=x
                while(x*k<n):
                    isPrime[x*k]=0
                    k+=1

        return len(Primes)
if __name__ == '__main__':
    print(Solution().countPrimes(10))
