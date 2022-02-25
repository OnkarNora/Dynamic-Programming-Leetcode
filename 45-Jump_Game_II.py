# https://leetcode.com/problems/jump-game-ii/
# https://www.youtube.com/watch?v=dJ7sWiOoK7g&list=PLot-Xpze53lcvx_tjrr_m2lgD2NsRHlNO&index=23

# My Solution with DP : (works but 17 seconds is a lot 😂)

class Solution:
    def jump(self, nums: List[int]) -> int:
        dp = {}
        def recurse(i):
            if (i>=(len(nums)-1)):
                return 0
            if i in dp:
                return dp[i]
            Min = len(nums) + 1
            for j in range(nums[i]):
                Min = min(Min, 1 + recurse(i+j+1))
            dp[i] = Min
            return dp[i]
        
        return recurse(0)

# Solution with Greedy approach : 
class Solution:
    def jump(self, nums: List[int]) -> int:
        res = 0
        l = r = 0
        
        while r < len(nums) - 1:
            farthest = 0
            for i in range(l, r + 1):
                farthest = max(farthest, i + nums[i])
            l = r + 1
            r = farthest
            res += 1
        return res