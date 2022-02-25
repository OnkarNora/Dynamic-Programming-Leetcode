# https://leetcode.com/problems/all-possible-full-binary-trees/
# https://www.youtube.com/watch?v=nZtrZPTTCAo&list=PLot-Xpze53lcvx_tjrr_m2lgD2NsRHlNO&index=37

# Solution without DP : (TLE)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def allPossibleFBT(self, n: int) -> List[Optional[TreeNode]]:
        
        # ret the list of fbt with n nodes
        def backtrack(n):
            if n == 0:
                return []
            if n == 1:
                return [TreeNode()]
            
            res = []
            for l in range(n): # 0 - (n - 1)
                r = n - 1 - l
                leftTrees, rightTrees = backtrack(l), backtrack(r)
                
                for t1 in leftTrees:
                    for t2 in rightTrees:
                        res.append(TreeNode(0, t1, t2))
            return res
        
        return backtrack(n)
                
            
# Solution with DP : 
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def allPossibleFBT(self, n: int) -> List[Optional[TreeNode]]:
        dp = { 0 : [], 1 : [TreeNode()]} # map n : list of FBT
        
        # ret the list of fbt with n nodes
        def backtrack(n):
            
            if n in dp:
                return dp[n]
            
            res = []
            for l in range(n): # 0 - (n - 1)
                r = n - 1 - l
                leftTrees, rightTrees = backtrack(l), backtrack(r)
                
                for t1 in leftTrees:
                    for t2 in rightTrees:
                        res.append(TreeNode(0, t1, t2))
            dp[n] = res
            return res
        
        return backtrack(n)
                
            