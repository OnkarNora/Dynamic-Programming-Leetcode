# https://leetcode.com/problems/burst-balloons/
# https://www.youtube.com/watch?v=VFskby7lUbw&list=PLot-Xpze53lcvx_tjrr_m2lgD2NsRHlNO&index=28

# My Solution with DP : (TLE)
class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        dp = {}
        def recurse(n):
            if len(n) == 0:
                return 0
            t = tuple(n)
            if t in dp:
                return dp[t]
            n.append(1)
            n.insert(0,1)
            coins = 0
            for i in range(1, len(n) - 1):
                coins = max(coins, n[i-1]*n[i]*n[i+1] + recurse(n[1:i]+n[i+1:len(n)-1]))
            dp[t] = coins
            return dp[t]
        return recurse(nums)

# Solution with DP : (TLE) # its really hard, understand with video if you really want to
class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        nums = [1] + nums + [1]
        dp = {}
        
        def dfs(l,r):
            if l > r:
                return 0
            if (l, r) in dp:
                return dp[(l,r)]
            
            dp[(l,r)] = 0
            for i in range(l, r + 1):
                coins = nums[l-1] * nums[i] * nums[r + 1]
                coins += dfs(l, i - 1) + dfs(i + 1, r)
                dp[(l,r)] = max(dp[(l,r)], coins)
            return dp[(l,r)]
            
        return dfs(1, len(nums) - 2)