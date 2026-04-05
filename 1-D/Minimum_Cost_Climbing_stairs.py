## memoization
def helper(i, arr, dp):
    if i == 0 or i == 1:
        return 0

    if dp[i] != -1:
        return dp[i]

    dp[i] = min(arr[i - 1] + helper(i - 1, arr, dp),
                arr[i - 2] + helper(i - 2, arr, dp))
    return dp[i]


## tabulation
def helper1(arr):
    n = len(arr)
    if n == 0 or n == 1:
        return 0

    dp = [0] * (n + 1)
    dp[0], dp[1] = 0, 0

    for i in range(2, n + 1):
        dp[i] = min(arr[i - 1] + dp[i - 1],
                    arr[i - 2] + dp[i - 2])

    return dp[n]


def minCostClimbingStairs(cost):
    return helper1(cost)


print(minCostClimbingStairs([1, 2, 3, 4, 5]))