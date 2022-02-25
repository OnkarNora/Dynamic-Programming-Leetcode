# https://leetcode.com/problems/partition-equal-subset-sum/
# https://www.youtube.com/watch?v=IsvocB5BJhw&list=PLot-Xpze53lcvx_tjrr_m2lgD2NsRHlNO&index=31

# My Solution with DP : (TLE)
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        dp = {}
        def recurse(s,i):
            if i>=len(nums):
                return s==0
            if (s,i) in dp:
                return dp[(s,i)]
            
            dp[(s,i)] = recurse(s+nums[i],i+1) or recurse(s-nums[i],i+1)
            return dp[(s,i)]
        
        return recurse(0,0)

# Solution with pure DP : (memory optimized)
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2:
            return False
        
        dp = set()
        dp.add(0)
        target = sum(nums) // 2
        
        for i in range(len(nums) -1,  -1, -1):
            nextDP = set()
            for t in dp:
                if (t + nums[i]) == target:
                    return True
                nextDP.add(t + nums[i])
                nextDP.add(t)
            dp = nextDP
            
        return True if target in dp else False