# https://leetcode.com/problems/maximum-alternating-subsequence-sum/
# https://www.youtube.com/watch?v=4v42XOuU1XA&list=PLot-Xpze53lcvx_tjrr_m2lgD2NsRHlNO&index=31

# My Solution with DP : (TLE)
class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        dp = {}
        def recurse(s,i,flag):
            if i>=len(nums):
                return s
            if (s,i,flag) in dp:
                return dp[(s,i,flag)]
            if flag:
                dp[(s,i,flag)] = max(recurse(s+nums[i],i+1,0),recurse(s,i+1,1))
                return dp[(s,i,flag)]
            else:
                dp[(s,i,flag)] = max(recurse(s-nums[i],i+1,1),recurse(s,i+1,0))
                return dp[(s,i,flag)]
        
        return recurse(0,0,1)

# Solution with DP : 
class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        dp = {}
        # i = index, even = true/false, total = current sum
        def dfs(i, even):
            if i == len(nums):
                return 0
            if (i,even) in dp:
                return dp[(i,even)]
            
            total = nums[i] if even else (-1 * nums[i])
            dp[(i,even)] = max(total + dfs(i + 1, not even), dfs(i + 1, even))
            return dp[(i,even)]
        return dfs(0,True)

# Solution with pure DP : (memory optimized)
class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        sumEven, sumOdd = 0, 0
        
        for i in range(len(nums) - 1, -1, -1):
            tmpEven = max(sumOdd + nums[i], sumEven)
            tmpOdd = max(sumEven - nums[i], sumOdd)
            sumEven, sumOdd = tmpEven, tmpOdd
            
        return sumEven