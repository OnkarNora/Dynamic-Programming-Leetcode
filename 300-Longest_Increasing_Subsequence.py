# https://leetcode.com/problems/longest-increasing-subsequence/
# https://www.youtube.com/watch?v=cjWnW0hdF1Y&list=PLot-Xpze53lcvx_tjrr_m2lgD2NsRHlNO&index=13&t=2s

# My Solution with DP:
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = {}
        def recurse(i):
            if i>=len(nums):
                return 0
            if i in dp:
                return dp[i]
            Max = 1
            for j in range(i+1,len(nums)):
                if nums[i] < nums[j]:
                    Max = max(Max,1 + recurse(j))
            dp[i] = Max
            return dp[i]
        for j in range(len(nums)):
            recurse(j)
        return max(dp.values())

# Solution with pure DP:

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        LIS = [1] * len(nums)
        
        for i in range(len(nums) - 1, -1, -1):
            for j in range(i + 1, len(nums)):
                if nums[i] < nums[j]:
                    LIS[i] = max(LIS[i], 1 + LIS[j])
                    
        return max(LIS)