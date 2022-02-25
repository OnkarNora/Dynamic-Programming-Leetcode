# https://leetcode.com/problems/delete-and-earn/
# https://www.youtube.com/watch?v=7FCemBxvGw0&list=PLot-Xpze53lcvx_tjrr_m2lgD2NsRHlNO&index=44

# Solution with pure DP : (Memory Optimized)

class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        count = Counter(nums)
        nums = sorted(list(set(nums)))
        
        earn1, earn2 = 0, 0
        for i in range(len(nums)):
            curEarn = nums[i] * count[nums[i]]
            # can't use both curEarn and earn2
            if i > 0 and nums[i] == nums[i - 1] + 1:
                temp = earn2
                earn2 = max(curEarn + earn1, earn2)
                earn1 = temp
            else:
                temp = earn2
                earn2 = curEarn + earn2
                earn1 = temp
        
        return earn2