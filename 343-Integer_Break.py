# https://leetcode.com/problems/integer-break/
# https://www.youtube.com/watch?v=in6QbUPMJ3I&list=PLot-Xpze53lcvx_tjrr_m2lgD2NsRHlNO&index=43

# My Solution with DP : 

class Solution:
    def integerBreak(self, n: int) -> int:
        dp = {}
        def recurse(i,s):
            if s==n:
                return 1
            if s>n or i>=n:
                return 0
            if (i,s) in dp:
                return dp[(i,s)]
            
            dp[(i,s)] = max(recurse(i,s + i)*i,recurse(i+1,s))
            return dp[(i,s)]
        
        return recurse(1,0)

# Solution with DP : 
class Solution:
    def integerBreak(self, n: int) -> int:
        dp = {1 : 1}
        
        def dfs(num):
            if num in dp:
                return dp[num]
            
            dp[num] = 0 if num == n else num 
            for i in range(1, num):
                val = dfs(i) * dfs(num - i)
                dp[num] = max(dp[num], val)
            return dp[num]
        
        return dfs(n)

# Solution with pure DP : 
class Solution:
    def integerBreak(self, n: int) -> int:
        dp = {1 : 1}
        
        for num in range(2, n + 1):
            dp[num] = 0 if num == n else num
            for i in range(1, num):
                val = dp[i] * dp[num - i]
                dp[num] = max(dp[num], val)
                
        return dp[n]