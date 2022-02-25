# https://leetcode.com/problems/word-break/
# https://www.youtube.com/watch?v=Sx9NNgInc3A&list=PLot-Xpze53lcvx_tjrr_m2lgD2NsRHlNO&index=6

# My solution Without DP: (TLE)

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        def recurse(i,j):
            # print(i,j)
            if i>=len(s) and i+1 == j:
                return True
            elif j>len(s):
                return False
                
            if s[i:j] not in wordDict:
                # print(s[i:j])
                return recurse(i,j+1)
            else:
                if recurse(j,j+1):
                    return True
                return recurse(i,j+1)
        return recurse(0,1)

# Solution With DP : 
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
        dp = [False] * (len(s) + 1)
        dp[len(s)] = True
        
        for i in range(len(s) - 1, -1, -1):
            for w in wordDict:
                if (i+len(w) <= len(s)) and s[i : i+len(w)] == w:
                    dp[i] = dp[i+len(w)]
                if dp[i]:
                    break
        return dp[0]
                    