# https://leetcode.com/problems/minimum-cost-for-tickets/submissions/
# https://www.youtube.com/watch?v=4pY1bsBpIY4&list=PLot-Xpze53lcvx_tjrr_m2lgD2NsRHlNO&index=3

# My solution with dp : 

class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        dp = {}
        def recurse(i):
            if i >= len(days):
                return 0
            if i in dp:
                return dp[i]
            x = i+1
            temp = days[i] + 6
            y = i
            while(y<len(days) and temp>=days[y]):
                y+=1
            temp = days[i] + 29
            z = i
            while(z<len(days) and temp>=days[z]):
                z += 1
            dp[i] = min(costs[0]+recurse(x),costs[1]+recurse(y),costs[2]+recurse(z))
            return dp[i]    
        
        return recurse(0)

# Solution with dp : 
class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        dp = {}
        
        def dfs(i):
            if i == len(days):
                return 0
            if i in dp:
                return dp[i]
            
            dp[i] = float("inf")
            for d,c in zip([1,7,30],costs):
                j = i
                while j<len(days) and days[j] < days[i] +d:
                    j+=1
                dp[i] = min(dp[i], c + dfs(j))
            return dp[i]
        
        return dfs(0)