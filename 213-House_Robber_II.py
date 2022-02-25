# https://leetcode.com/problems/house-robber-ii/
# https://www.youtube.com/watch?v=rWAJCfYYOvM&list=PLot-Xpze53lcvx_tjrr_m2lgD2NsRHlNO&index=11

# Solution with pure DP:
class Solution:
    def rob(self, nums: List[int]) -> int:
        
        return max(nums[0],self.helper(nums[1:]),self.helper(nums[:-1]))
        
    def helper(self,nums): #This is just House Robber I
        rob1,rob2 = 0,0

        for n in nums:
            newRob = max(rob1 + n, rob2)
            rob1 = rob2
            rob2 = newRob

        return rob2