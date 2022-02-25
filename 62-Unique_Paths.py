# https://leetcode.com/problems/unique-paths/
# https://www.youtube.com/watch?v=IlEsdxuD4lY&list=PLot-Xpze53lcvx_tjrr_m2lgD2NsRHlNO&index=23

# My Solution with DP : 
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = {}
        def recurse(i,j):
            if i == m-1 and j == n-1:
                return 1
            if i>=m or j>=n:
                return 0
            if (i,j) in dp:
                return dp[(i,j)]
            dp[(i,j)] = recurse(i + 1, j) + recurse(i, j + 1)
            return dp[(i,j)]
        
        return recurse(0,0)

# Solution with pure DP : (memory optimized):
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        row = [1] * n
        
        for i in range(m - 1):
            newRow = [1] * n
            for j in range(n - 2, -1, -1):
                newRow[j] = newRow[j+1] + row[j]
            row = newRow
        return row[0]