# https://leetcode.com/problems/pascals-triangle/
# https://www.youtube.com/watch?v=nPVEaB3AjUM&list=PLot-Xpze53lcvx_tjrr_m2lgD2NsRHlNO&index=37

# My Solution with pure DP : 
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 1:
            return [[1]]
        elif numRows == 2:
            return [[1],[1,1]]
        ans = [[1],[1,1]]
        
        for i in range(2, numRows ):
            ans.append([1])
            for j in range(0,i - 1):
                ans[i].append(ans[i - 1][j] + ans[i - 1][j + 1])
            ans[i].append(1)
            
        return ans

# Solution with pure DP : 
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = [[1]]
        for i in range(numRows - 1):
            temp = [0] + res[-1] + [0]
            row = []
            for j in range(len(res[-1]) + 1):
                row.append(temp[j] + temp[j + 1])
            res.append(row)
        return res