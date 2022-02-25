# https://leetcode.com/problems/maximal-square/
# https://www.youtube.com/watch?v=6X7Ha2PrDmM&list=PLot-Xpze53lcvx_tjrr_m2lgD2NsRHlNO&index=17

# My Solution with DP : (kinda wanted to tru bottom up true dp but didn't)
class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        dp = {}
        n,m = len(matrix),len(matrix[0])
        def recurse(i,j):
            if i+1>=n or j+1>= m:
                dp[(i,j)] = 1 if matrix[i][j] == "1" else 0
                return dp[(i,j)]
            if (i,j) in dp:
                return dp[(i,j)]
            if matrix[i][j] == "1":
                dp[(i,j)] = 1 + min(recurse(i+1,j),recurse(i,j+1),recurse(i+1,j+1))
                return dp[(i,j)]
            dp[(i,j)] = 0
            return 0
        for i in range(n):
            for j in range(m):
                recurse(i,j)
        print(dp)
        a = max(dp.values())
        return a*a

# Solution with DP : (recursive TOP DOWN)
class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        # dynamic programming bottom up
        # recursive: top down (this one)
        
        ROWS, COLS = len(matrix), len(matrix[0])
        cache = {} # map each (r,c) -> maxLength of square
        
        def helper(r, c):
            if r >= ROWS or c >=COLS:
                return 0
            
            if (r,c) not in cache:
                down = helper(r + 1, c)
                right = helper(r, c + 1)
                diag = helper(r + 1, c + 1)
                
                cache[(r,c)] = 0
                if matrix[r][c] == "1":
                    cache[(r,c)] = 1 + min(down, right, diag)
            
            
            return cache[(r,c)]
        
        helper(0,0)
        return max(cache.values()) ** 2