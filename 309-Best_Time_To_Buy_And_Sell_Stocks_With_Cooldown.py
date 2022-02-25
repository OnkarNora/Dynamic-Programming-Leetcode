# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/
# https://www.youtube.com/watch?v=I7j0F7AHpb8&list=PLot-Xpze53lcvx_tjrr_m2lgD2NsRHlNO&index=41

# My Solution with DP : 
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = {}
        def recurse(i,buy):
            if i>=len(prices):
                return 0
            if (i,buy) in dp:
                return dp[(i,buy)]
            
            if buy:
                dp[(i,buy)] = max(recurse(i+1,not buy) - prices[i],recurse(i+1,buy))
            else:
                dp[(i,buy)] = max(recurse(i + 2,not buy) + prices[i],recurse(i+1,buy))
            return dp[(i,buy)]
        
        return recurse(0,True)
        
# Solution with DP : 
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = {}
        
        def dfs(i, buying):
            if i >= len(prices):
                return 0
            if (i, buying) in dp:
                return dp[(i,buying)]
            
            if buying:
                buy = dfs(i + 1, not buying) - prices[i]
                cooldown = dfs(i + 1, buying)
                dp[(i, buying)] = max(buy, cooldown)
            else:
                sell = dfs(i + 2, not buying) + prices[i]
                cooldown = dfs(i + 1, buying)
                dp[(i,buying)] = max(sell, cooldown)
            return dp[(i,buying)]
        
        return dfs(0, True)
        