# https://leetcode.com/problems/interleaving-string/
# https://www.youtube.com/watch?v=3Rw3p9LrgvE&list=PLot-Xpze53lcvx_tjrr_m2lgD2NsRHlNO&index=10

# My Solution with DP : (still not able to figure out pure DP)
class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        dp = {}
        def recurse(i,j,k):
            if (k>=len(s3)):
                if i>=len(s1) and j>=len(s2):
                    return True
                return False
            if ((i,j,k) in dp):
                return dp[(i,j,k)]
            if i<len(s1) and j<len(s2) and (s1[i] == s2[j]) and (s1[i] == s3[k]):
                dp[(i,j,k)] = (recurse(i+1,j,k+1) or recurse(i,j+1,k+1))
                return dp[(i,j,k)]
            if i<len(s1) and s1[i] == s3[k]:
                dp[(i,j,k)] = recurse(i+1,j,k+1)
                return dp[(i,j,k)]
            if j<len(s2) and s2[j] == s3[k]:
                dp[(i,j,k)] = recurse(i,j+1,k+1)
                return dp[(i,j,k)]
            return False
        return recurse(0,0,0)

# Solution with pure DP:
class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3):
            return False
        dp = [ [False] * (len(s2) + 1) for i in range(len(s1) + 1)]
        dp[len(s1)][len(s2)] = True
        
        for i in range(len(s1), -1, -1):
            for j in range(len(s2), -1, -1):
                if i<len(s1) and s1[i] == s3[i+j] and dp[i + 1][j]:
                    dp[i][j] = True
                if j<len(s2) and s2[j] == s3[i+j] and dp[i][j + 1]:
                    dp[i][j] = True
        return dp[0][0]