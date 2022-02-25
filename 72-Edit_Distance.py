# https://leetcode.com/problems/edit-distance/
# https://www.youtube.com/watch?v=XYi2-LPrwm4&list=PLot-Xpze53lcvx_tjrr_m2lgD2NsRHlNO&index=25

# My Solution with DP : (after video)
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        dp = {}
        def recurse(i,j):
            if (i,j) in dp:
                return dp[(i,j)]
            if i>=len(word1) and j>=len(word2):
                return 0
            if i>=len(word1):
                return len(word2)-j
            if j>=len(word2):
                return len(word1)-i
            
            if word1[i] == word2[j]:
                dp[(i,j)] = recurse(i+1,j+1)
                return dp[(i,j)]
            
            dp[(i,j)] = 1 + min(recurse(i+1,j+1),recurse(i,j+1),recurse(i+1,j))
            return dp[(i,j)]
        
        return recurse(0,0)

# Solution with pure DP : 
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        cache = [ [float('inf')] * (len(word2) + 1) for i in range(len(word1) + 1)]
        
        for j in range(len(word2) + 1):
            cache [len(word1)][j] = len(word2) - j
        for i in range(len(word1) + 1):
            cache[i][len(word2)] = len(word1) - i
            
        for i in range(len(word1) - 1, -1, -1):
            for j in range(len(word2) - 1, -1, -1):
                if word1[i] == word2[j]:
                    cache[i][j] = cache[i + 1][j + 1]
                else:
                    cache[i][j] = 1 + min(cache[i + 1][j],cache[i][j + 1],cache[i+1][j+1])
        
        return cache[0][0]