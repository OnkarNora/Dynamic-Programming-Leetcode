# https://leetcode.com/problems/paint-house/ or # https://www.lintcode.com/problem/515/
# https://www.youtube.com/watch?v=-w67-4tnH5U&list=PLot-Xpze53lcvx_tjrr_m2lgD2NsRHlNO&index=12

# My solution with DP :
class Solution:
    def solve(self, A):
        dp = {}
        def recurse(i,j):
            if i>=len(A):
                return 0
            if (i,j) in dp:
                return dp[(i,j)]
            Min = float("inf")
            for k in range(3):
                if k!=j:
                    Min = min(Min,A[i][k] + recurse(i+1,k))
            dp[(i,j)] = Min
            return dp[(i,j)]
        if len(A) == 0:
            return 0
        return min(A[0][0] + recurse(1,0), A[0][1] + recurse(1,1), A[0][2] + recurse(1,2))

# Solution with True DP: (memory optimized)

class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        # cost[i][j] i is house, j is color

        dp = [0,0,0]

        for i in range(len(costs)):
            dp0 = costs[i][0] + min(dp[1],dp[2])
            dp1 = costs[i][1] + min(dp[0],dp[2])
            dp2 = costs[i][2] + min(dp[0],dp[1])
            dp = [dp0,dp1,dp2]

        return min(dp)