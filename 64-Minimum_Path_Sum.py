# https://leetcode.com/problems/minimum-path-sum/
# https://www.youtube.com/watch?v=pGMsrvt0fpk&list=PLot-Xpze53lcvx_tjrr_m2lgD2NsRHlNO&index=35

# My Solution with DP : 
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        dp = {}
        def recurse(i,j):
            if (i,j) in dp:
                return dp[(i,j)]
            if i == len(grid)-1 and j == len(grid[0])-1:
                return grid[i][j]
            if i>=len(grid) or j>=len(grid[0]):
                return float('inf')
            dp[(i,j)] = grid[i][j] + min(recurse(i+1,j),recurse(i,j+1))
            return dp[(i,j)]
        
        return recurse(0,0)

# Solution with pure DP : (can be memory optimized)

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        
        res = [[float('inf')] * (COLS + 1) for r in range(ROWS + 1)]
        res[ROWS - 1][COLS] = 0
        
        for r in range(ROWS - 1, -1, -1):
            for c in range(COLS - 1, -1, -1):
                res[r][c] = grid[r][c] + min(res[r + 1][c], res[r][c + 1])
        return res[0][0]
        