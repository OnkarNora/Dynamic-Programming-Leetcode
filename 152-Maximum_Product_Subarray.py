# https://leetcode.com/problems/maximum-product-subarray/
# https://www.youtube.com/watch?v=lXVy6YWFcRM&list=PLot-Xpze53lcvx_tjrr_m2lgD2NsRHlNO&index=15&t=1s

# Solution with pure DP:

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = max(nums)
        curMin, curMax = 1, 1
        
        for n in nums:
            if n == 0:
                curMin, curMax = 1, 1
                continue
            
            tmp = curMax * n
            curMax = max(n * curMax, n * curMin, n) 
            curMin = min(tmp, n * curMin, n)
            # print(curMax, curMin)
            res = max(res, curMax)
            
        return res
            
        