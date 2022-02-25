# https://leetcode.com/problems/minimum-number-of-days-to-eat-n-oranges/
# https://www.youtube.com/watch?v=LziQ6Qx9sks&list=PLot-Xpze53lcvx_tjrr_m2lgD2NsRHlNO&index=34

# My Solution with DP : (TLE)
class Solution:
    def minDays(self, n: int) -> int:
        dp = {}
        def recurse(n):
            
            if n <= 2:
                dp[n] = n
                return dp[n]
            if n in dp:
                return dp[n]
            if n%2 == 0 and n%3 == 0:
                dp[n] = 1 + min(recurse(n-1),recurse(n - n//2),recurse(n - 2*(n//3)))
                return dp[n]
            if n%2 == 0:
                dp[n] = 1 + min(recurse(n-1),recurse(n - n//2))
                return dp[n]
            if n%3 == 0:
                dp[n] = 1 + min(recurse(n-1),recurse(n - 2*(n//3)))
                return dp[n]
            dp[n] = 1 + recurse(n-1)
            return dp[n]
        
        return recurse(n)
        
# Solution with DP : 
class Solution:
    def minDays(self, n: int) -> int:
        dp = { 0 : 0, 1 : 1}
        
        def dfs(n):
            if n in dp:
                return dp[n]
            
            one = 1 + (n%2) + dfs(n // 2)
            two = 1 + (n%3) + dfs(n // 3)
            dp[n] = min(one,two)
            return dp[n]
        
        return dfs(n)

# There is also a bfs solution to this you might wanna try 