## Tabulation
def robber(nums):
    n=len(nums)

    if n==1:return nums[0]
    if n==2:return max(nums[0],nums[1])

    dp=[0]*n
    dp[0]=nums[0]
    dp[1]=max(nums[0],nums[1])

    for i in range(2,n):
        dp[i]=max(nums[i]+dp[i-2],dp[i-1])
    return dp[n-1]


##Memoization
def robbery(i,nums,dp):
    if i==0:return nums[0]
    if i==1:return max(nums[0],nums[1])

    if dp[i]!=-1:
        return dp[i]

    dp[i]=max(nums[i]+robbery(i-2,nums,dp),robber(i-1,nums,dp))
    return dp[i]


