# https://leetcode.com/problems/counting-bits/
# https://www.youtube.com/watch?v=LziQ6Qx9sks&list=PLot-Xpze53lcvx_tjrr_m2lgD2NsRHlNO&index=34

# Solution with pure DP : 

class Solution:
    def countBits(self, n: int) -> List[int]:
        dp = [0] * (n + 1)
        offset = 1
        for i in range(1, n + 1):
            if offset * 2 == i:
                offset = i
            dp[i] = 1 + dp[i - offset]
            
        return dp