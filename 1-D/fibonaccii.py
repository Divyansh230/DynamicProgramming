from typing import List

## Fibonacci series using memoization
def fibo(n:int,dp:List[int])->int:
    if n <= 1:return n
    if dp[n] != -1:return dp[n]
    dp[n] = fibo(n-1,dp) + fibo(n-2,dp)
    return dp[n]

## Tabulation
def fiboTab(n:int)->int:
    dp=[0]*(n+1)
    dp[1]=1
    for i in range(2,n+1):
        dp[i] = dp[i-1] + dp[i-2]
    return dp[n]

#Space optimized
def fiboSpace(n:int)->int:
    if n <= 1:return n
    a,b=0,1
    for i in range(2,n+1):
        c = a + b
        a,b = b,c
    return b
    
n=int(input("Enter the number: "))
dp=[-1]*(n+1)
print(fibo(n,dp))