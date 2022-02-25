# https://leetcode.com/problems/longest-increasing-path-in-a-matrix/
# https://www.youtube.com/watch?v=wCc_nd-GiEc&list=PLot-Xpze53lcvx_tjrr_m2lgD2NsRHlNO&index=45

# My Solution with DP : 

class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        n, m = len(matrix), len(matrix[0])
        dp = {}
        def recurse(i,j):
            if (i,j) in dp:
                return dp[(i,j)]
            a,b,c,d = 1,1,1,1
            if i < n and j + 1 < m and matrix[i][j + 1] > matrix[i][j]:
                a = 1 + recurse(i,j + 1)
            if i + 1 < n and j < m and matrix[i + 1][j] > matrix[i][j]:
                b = 1 + recurse(i + 1, j)
            if i < n and j - 1 >= 0 and matrix[i][j - 1] > matrix[i][j]:
                c = 1 + recurse(i,j - 1)
            if i - 1 >= 0 and j < m and matrix[i - 1][j] > matrix[i][j]:
                d = 1 + recurse(i - 1, j)
            dp[(i,j)] = max(a,b,c,d)
            return dp[(i,j)]
        Max = 1
        for i in range(n):
            for j in range(m):
                temp = recurse(i,j)
                if temp > Max:
                    Max = temp
        return Max
        
# Solution with DP : 
class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        ROWS, COLS = len(matrix), len(matrix[0])
        dp = {}
        
        def dfs(r, c, prevVal):
            if(r < 0 or r == ROWS or
               c < 0 or c == COLS or
               matrix[r][c] <= prevVal):
                return 0
            if (r, c) in dp:
                return dp[(r, c)]
            
            res = 1
            res = max(res, 1 + dfs(r + 1, c, matrix[r][c]))
            res = max(res, 1 + dfs(r - 1, c, matrix[r][c]))
            res = max(res, 1 + dfs(r, c + 1, matrix[r][c]))
            res = max(res, 1 + dfs(r, c - 1, matrix[r][c]))
            dp[(r, c)] = res
            return res
        
        for r in range(ROWS):
            for c in range(COLS):
                dfs(r, c, -1)
        return max(dp.values())