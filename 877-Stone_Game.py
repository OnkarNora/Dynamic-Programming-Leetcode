# https://leetcode.com/problems/stone-game/
# https://www.youtube.com/watch?v=uhgdXOlGYqE&list=PLot-Xpze53lcvx_tjrr_m2lgD2NsRHlNO&index=39

# My Solution with DP : (5 sec)
class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        dp = {}
        def recurse(i,j,sa,sb):
            if i > j:
                return sa > sb
            if (i,j,sa,sb) in dp:
                return dp[(i,j,sa,sb)]
            if (j - i)%2:
                dp[(i,j,sa,sb)] = (recurse(i+1,j,sa+piles[i],sb) or recurse(i,j-1,sa+piles[j],sb))
            else:
                dp[(i,j,sa,sb)] = (recurse(i+1,j,sa,sb+piles[i]) or recurse(i,j-1,sa,sb+piles[j]))
            return dp[(i,j,sa,sb)]
        
        return recurse(0,len(piles) - 1,0,0)

# Trick you can just return True to pass all test cases (😂) Explaination is in video

# Solution with DP : 
class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        dp = {} # subarr piles (l, r) -> Max Alice Total
        
        # Return: Max Alice Total
        def dfs(l, r):
            if l > r:
                return 0
            if (l, r) in dp:
                return dp[(l, r)]
            
            even = True if (r - l) % 2 else False
            left = piles[l] if even else 0
            right = piles[r] if even else 0
            
            dp[(l, r)] = max(dfs(l + 1, r) + left, dfs(l, r - 1) + right)
            
            return dp[(l, r)]
        return dfs(0, len(piles) - 1) > (sum(piles))//2
            