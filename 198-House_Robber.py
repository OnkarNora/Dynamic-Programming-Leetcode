# https://leetcode.com/problems/house-robber/
# https://www.youtube.com/watch?v=73r3KWiEvyk&list=PLot-Xpze53lcvx_tjrr_m2lgD2NsRHlNO&index=9

# My solution with DP: (wanted to try pure DP solution but did not)
class Solution:
    def rob(self, nums: List[int]) -> int:
        dp = {}
        def recurse(i):
            if (i>=len(nums)):
                return 0
            if i in dp:
                return dp[i]
            dp[i] = max(recurse(i+1),nums[i] + recurse(i+2))
            return dp[i]
        return recurse(0)

# Solution with pure DP:(memory optimized)
class Solution:
    def rob(self, nums: List[int]) -> int:
        rob1,rob2 = 0,0
        
        # [rob1,rob2,n,n+1, ...]
        for n in nums:
            temp = max(n + rob1, rob2)
            rob1 = rob2
            rob2 = temp
        return rob2