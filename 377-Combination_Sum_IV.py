# https://leetcode.com/problems/combination-sum-iv/
# https://www.youtube.com/watch?v=dw2nMCxG0ik&list=PLot-Xpze53lcvx_tjrr_m2lgD2NsRHlNO&index=27&t=2s

# My Solution with DP : 
class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        dp = {}
        def recurse(s):
            if s == 0:
                return 1
            if s<0:
                return 0
            if s in dp:
                return dp[s]
            Sum = 0
            for j in range(len(nums)):
                Sum += recurse(s-nums[j])
            dp[s] = Sum
            return dp[s]
        
        return recurse(target)

# Solution with pure DP : 
class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        dp = { 0 : 1 }
        
        for total in range(1, target + 1):
            dp[total] = 0
            for n in nums:
                dp[total] += dp.get(total - n,0)
                
        return dp[total]
        