# https://leetcode.com/problems/target-sum/
# https://www.youtube.com/watch?v=g0npyaQtAQM&list=PLot-Xpze53lcvx_tjrr_m2lgD2NsRHlNO&index=1

# My solution without dp : 
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        def count(i,su):
            if i == len(nums):
                if su == target:
                    return 1
                return 0
            return (count(i+1,su+nums[i])+count(i+1,su-nums[i]))
        return count(0,0)

# solution with dp : 
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        dp = {} # (index,total) -> # of ways
        
        def backtrack(i,total):
            if i == len(nums):
                return 1 if total == target else 0
            if (i,total) in dp:
                return dp[(i,total)]
            dp[(i,total)] = (backtrack(i+1,total + nums[i]) +
                             backtrack(i+1,total - nums[i]))
            return dp[(i,total)]
        return backtrack(0,0)