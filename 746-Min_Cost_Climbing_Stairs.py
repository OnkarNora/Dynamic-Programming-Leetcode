# https://leetcode.com/problems/min-cost-climbing-stairs/
# https://www.youtube.com/watch?v=ktmzAZWkEZ0&list=PLot-Xpze53lcvx_tjrr_m2lgD2NsRHlNO&index=38

# My Solution with DP : 
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dp = {}
        def recurse(i):
            if i >= len(cost):
                return 0
            if i in dp:
                return dp[i]
            dp[i] = cost[i] + min(recurse(i + 1),recurse(i + 2))
            return dp[i]
        
        return min(recurse(0),recurse(1))

# Solution with pure DP : (memory optimized)
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        cost.append(0)
        
        for i in range(len(cost) - 3, -1, -1):
            cost[i] += min(cost[i + 1], cost[i + 2])
        
        return min(cost[0], cost[1])