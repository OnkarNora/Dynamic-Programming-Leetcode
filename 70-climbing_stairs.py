# https://leetcode.com/problems/climbing-stairs/submissions/
# https://www.youtube.com/watch?v=Y0lT9Fck7qI&list=PLot-Xpze53lcvx_tjrr_m2lgD2NsRHlNO&index=2

# My solution with dp : # insted of storing all n values you can store only previous two values but i didn't do that
class Solution:
    def climbStairs(self, n: int) -> int:
        dp = {}
        def recurse(n):
            if n in dp:
                return dp[n]
            if n == 0:
                return 1
            if n<0:
                return 0
            dp[n] = (recurse(n-1) + recurse(n-2))
            return dp[n]
        return recurse(n)

# Solution with dp : 
class Solution:
    def climbStairs(self, n: int) -> int:
        one, two = 1,1
        
        for i in range(n-1):
            temp = one
            one = one + two
            two = temp
            
        return one