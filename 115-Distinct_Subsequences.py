# https://leetcode.com/problems/distinct-subsequences/submissions/
# https://www.youtube.com/watch?v=-RDzMJ33nx8&list=PLot-Xpze53lcvx_tjrr_m2lgD2NsRHlNO&index=27

# My Solution with DP : 
class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        dp = {}
        def recurse(i,j):
            if i>=len(s) and j>=len(t):
                return 1
            if j>=len(t):
                return 1
            if i>=len(s):
                return 0
            if (i,j) in dp:
                return dp[(i,j)]
            
            if s[i] == t[j]:
                dp[(i,j)] = recurse(i+1,j+1) + recurse(i+1,j)
                return dp[(i,j)]
            dp[(i,j)] = recurse(i+1,j)
            return dp[(i,j)]
        
        return recurse(0,0)

# Solution with DP : 
class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        cache = {}
        
        def dfs(i, j):
            if j == len(t):
                return 1
            if i == len(s):
                return 0
            if (i, j) in cache:
                return cache[(i,j)]
            
            if s[i] == t[j]:
                cache[(i,j)] = dfs(i + 1, j + 1) + dfs(i + 1, j)
            else:
                cache[(i,j)] = dfs(i + 1, j)
            return cache[(i,j)]
        
        return dfs(0,0)