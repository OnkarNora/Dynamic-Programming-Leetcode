# https://leetcode.com/problems/coin-change-2/
# https://www.youtube.com/watch?v=Mjy4hd2xgrs&list=PLot-Xpze53lcvx_tjrr_m2lgD2NsRHlNO&index=4

# My solution with dp but TLE : 
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = {}
        def recurse(i,a):
            if a == amount:
                return 1
            if a > amount :
                return 0
            if (i,a) in dp:
                return dp[(i,a)]
            su = 0
            j = i
            while(j<len(coins)):
                su +=  recurse(j,a + coins[j])
                j += 1
            dp[(i,a)] = su
            return dp[(i,a)]
        return recurse(0,0)

# Solution with DP : 
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        cache = {}
        
        def dfs(i, a):
            if a == amount :
                return 1
            if a > amount :
                return 0
            if i == len(coins):
                return 0
            if (i,a) in cache:
                return cache[(i,a)]
            
            cache[(i,a)] = dfs(i, a + coins[i]) + dfs (i + 1, a)
            return cache[(i,a)]
        
        return dfs(0,0)

# Solution with DP with complete 2D array
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [[0] * (len(coins)+1) for i in range(amount+1)]
        dp[0] = [1] * (len(coins) + 1)
        
        for a in range(1,amount + 1):
            for i in range(len(coins)-1,-1,-1):
                dp[a][i] = dp[a][i+1]
                if a - coins[i] >= 0:
                    dp[a][i] += dp[a-coins[i]][i]
        return dp[amount][0]

# Solution with DP with Memory optimization : (or pure DP Solution also check memory optimized Knapsack for this)
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [0] * (amount + 1)
        dp[0] = 1
        
        for i in range(len(coins)-1,-1,-1):
            nextDP = [0] * (amount + 1)
            nextDP[0] = 1
            
            for a in range(1, amount + 1):
                nextDP[a] = dp[a]
                if a - coins[i] >= 0:
                    nextDP[a] += nextDP[a-coins[i]]
            dp = nextDP
        return dp[amount]