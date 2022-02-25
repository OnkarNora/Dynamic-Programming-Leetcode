# https://leetcode.com/problems/triangle/
# https://www.youtube.com/watch?v=OM1MTokvxs4&list=PLot-Xpze53lcvx_tjrr_m2lgD2NsRHlNO&index=19

# My Solution with DP :
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        dp = {}
        def recurse(i,j):
            if i>=len(triangle):
                return 0
            if (i,j) in dp:
                return dp[(i,j)]
            dp[(i,j)] =  min(triangle[i][j] + recurse(i+1,j),triangle[i][j] + recurse(i+1,j+1))
            return dp[(i,j)]
        
        return recurse(0,0)
        
# Solution with pure DP : (memory optimized)
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        dp = [0] * (len(triangle) + 1)
        
        for row in triangle[::-1]:
            for i, n in enumerate(row):
                dp[i] = n + min(dp[i], dp[i+1])
                
        return dp[0]