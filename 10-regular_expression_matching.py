# https://leetcode.com/problems/regular-expression-matching/
# https://www.youtube.com/watch?v=HAA8mgxlov8

# without DP :
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        # Top-down Memoization 
        
        def dfs(i,j):
            if i>= len(s) and j>= len(p):
                return True
            if j >= len(p):
                return False
            
            match = i < len(s) and (s[i] == p[j] or p[j] == '.')
            
            if (j+1) < len(p) and p[j + 1] == '*':
                return (dfs(i,j+2) or # dont use *
                        (match and dfs(i+1,j))) # use * 
            if match:
                return dfs(i+1,j+1)
            
            return False
        
        return dfs(0,0)

# with DP :
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        # Top-down Memoization 
        
        cache = {}
        
        def dfs(i,j):
            if (i,j) in cache:
                return cache[(i,j)]
            if i>= len(s) and j>= len(p):
                return True
            if j >= len(p):
                return False
            
            match = i < len(s) and (s[i] == p[j] or p[j] == '.')
            
            if (j+1) < len(p) and p[j + 1] == '*':
                cache[(i,j)] = (dfs(i,j+2) or # dont use *
                        (match and dfs(i+1,j))) # use * 
                return cache[(i,j)]
            if match:
                cache[(i,j)] = dfs(i+1,j+1)
                return cache[(i,j)]
            cache[(i,j)] = False
            return cache[(i,j)]
        
        return dfs(0,0)