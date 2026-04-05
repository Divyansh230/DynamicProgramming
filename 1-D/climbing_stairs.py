## Memoization
def climb_stairs(n, dp):
    if n==0:return 1
    if n<0:return 0
    if dp[n]!=-1:return dp[n]
    dp[n] = climb_stairs(n-1, dp) + climb_stairs(n-2, dp)
    return dp[n]

## Tabulation
def climb_stairs_tab(n):
    if n==0 or n==1:return 1

    dp = [0]*(n+1)
    dp[0],dp[1] = 1,1
    for i in range(2, n+1):
        dp[i] = dp[i-1] + dp[i-2]
    return dp[n]

## Space optimized
def climb_stairs_space(n):
    if n==0 or n==1:return 1

    a,b = 1,1
    for i in range(2, n+1):
        c = a + b
        a,b = b,c
    return b