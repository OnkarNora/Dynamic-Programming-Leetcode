# https://leetcode.com/problems/perfect-squares/
# https://www.youtube.com/watch?v=HLZLwjzIVGo&list=PLot-Xpze53lcvx_tjrr_m2lgD2NsRHlNO&index=24

# My Solution with DP : (TLE)
class Solution:
    def numSquares(self, n: int) -> int:
        ps = []
        i = 1
        while(i*i <= n):
            ps.append(i*i)
            i += 1
        dp = {}
        def recurse(i,a):
            if a == n :
                return 0
            if (i,a) in dp:
                return dp[(i,a)]
            if a>n:
                return n
            if i>=len(ps):
                return n
            dp[(i,a)] = min(1 + recurse(i,ps[i] + a),recurse(i+1,a))
            return dp[(i,a)]
        return recurse(0,0)

# Solution with pure DP : 
class Solution:
    def numSquares(self, n: int) -> int:
        dp = [n] * (n + 1)
        dp[0] = 0
        
        for target in range(1, n + 1):
            for s in range(1, target + 1):
                square = s * s
                if target - square < 0:
                    break
                dp[target] = min(dp[target], 1 + dp[target - square])
                
        return dp[n]