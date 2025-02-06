class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        rows,cols=len(grid),len(grid[0])
        ans=0

        def helper(row,col):
            # check the boundary, if it is out of boundary return 0 as nothing found
            if row < 0 or row >= rows or col < 0 or col >= cols or grid[row][col] == 0:
                return 0

            temp=grid[row][col]
            grid[row][col]=0 # means marked visited

            ans=temp+max(helper(row-1,col) , helper(row+1,col) , helper(row,col+1) , helper(row,col-1))

            grid[row][col]=temp
            return ans




        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c]!=0:
                    ans=max(ans,helper(r,c))

        return ans