# https://leetcode.com/problems/jump-game/
# https://www.youtube.com/watch?v=dJ7sWiOoK7g&list=PLot-Xpze53lcvx_tjrr_m2lgD2NsRHlNO&index=22

# Solution with Greedy approach O(n) :
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        goal = len(nums) - 1
        
        for i in range(len(nums) - 1, -1, -1):
            if i + nums[i] >= goal:
                goal = i
        
        return True if goal == 0 else False

