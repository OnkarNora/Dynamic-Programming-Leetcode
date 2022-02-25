# https://leetcode.com/problems/longest-common-subsequence/
# https://www.youtube.com/watch?v=Ua0GhsJSlWM&list=PLot-Xpze53lcvx_tjrr_m2lgD2NsRHlNO&index=14

# My Solution with DP:
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dp = {}
        def recurse(i,j):
            if i>=len(text1) or j>=len(text2):
                return 0
            if (i,j) in dp:
                return dp[(i,j)]
            if text1[i] == text2[j]:
                dp[(i,j)] = 1 + recurse(i+1,j+1)
                return dp[(i,j)]
            dp[(i,j)] = max(recurse(i + 1, j),recurse(i, j + 1),recurse(i + 1, j + 1))
            return dp[(i,j)]
        return recurse(0,0)
        
# Solution with pure DP: (Bottom UP)
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dp = [[0 for j in range(len(text2) + 1)] for i in range(len(text1) + 1)]
        
        for i in range(len(text1) - 1, -1, -1):
            for j in range(len(text2) - 1, -1, -1):
                if text1[i] == text2[j]:
                    dp[i][j] = 1 + dp[i + 1][j + 1]
                else:
                    dp[i][j] = max(dp[i][j + 1],dp[i + 1][j])
        return dp[0][0]