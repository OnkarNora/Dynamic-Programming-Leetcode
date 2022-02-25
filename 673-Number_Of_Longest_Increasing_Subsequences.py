# https://leetcode.com/problems/number-of-longest-increasing-subsequence/
# https://www.youtube.com/watch?v=Tuc-rjJbsXU&list=PLot-Xpze53lcvx_tjrr_m2lgD2NsRHlNO&index=42

# My Solution with DP : 

class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        dp = {}
        a = [1] * (len(nums))
        def recurse(i):
            if i>=len(nums):
                return 0
            if i in dp:
                return dp[i]
            
            Max = 1
            count = 1
            for j in range(i+1,len(nums)):
                if nums[i] < nums[j]:
                    temp = 1 + recurse(j)
                    if temp == Max:
                        count += a[j]
                    if temp > Max:
                        Max = temp
                        count = a[j]
                    
            a[i] = count
            dp[i] = Max
            return dp[i]
        
        for i in range(len(nums)):
            recurse(i)
        
        b = []
        MaxLength = max(dp.values())
        for i,j in dp.items():
            if j == MaxLength:
                b.append(i)
        count = 0
        for i in b:
            count += a[i]
        return count
        
# Solution with DP : 
class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        # 1. O(n^2) Recursive solution with Caching
        
        dp = {} # key = index, value = [length of LIS, count]
        lenLIS, res = 0, 0 # length of LIS, count of LIS
        
        def dfs(i):
            if i in dp: return dp[i]
            
            maxLen, maxCnt = 1, 1 # length and count of LIS
            for j in range(i + 1, len(nums)):
                if nums[j] > nums[i]: # make sure increasing order
                    length, count = dfs(j)
                    if length + 1 > maxLen:
                        maxLen, maxCnt = length + 1, count
                    elif length + 1 == maxLen:
                        maxCnt += count   
            nonlocal lenLIS, res
            if maxLen > lenLIS:
                lenLIS, res = maxLen, maxCnt
            elif maxLen == lenLIS:
                res += maxCnt
            dp[i] = [maxLen, maxCnt]
            return dp[i]

        for i in range(len(nums)): dfs(i)
        return res

# Solution with pure DP : 
class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        # 2. O(n^2) Dynamic Programming 
        
        dp = {} # key = index, value = [length of LIS, count]
        lenLIS, res = 0, 0 # length of LIS, count of LIS
        
        # i = start of subseq
        for i in range(len(nums) - 1, -1, -1):
            maxLen, maxCnt = 1, 1 # len, cnt of LIS start from i
            
            for j in range(i + 1, len(nums)):
                if nums[j] > nums[i]:
                    length, count = dp[j] # len, cnt of LIS start from j
                    if length + 1 > maxLen:
                        maxLen, maxCnt = length + 1, count
                    elif length + 1 == maxLen:
                        maxCnt += count
            if maxLen > lenLIS:
                lenLIS, res = maxLen, maxCnt
            elif maxLen == lenLIS:
                res += maxCnt
            dp[i] = [maxLen, maxCnt]
                
        return res