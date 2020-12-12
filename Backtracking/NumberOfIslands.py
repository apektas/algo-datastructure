# DFS solution
class Solution:
    def numIslands(self, grid):
        if not (grid or grid[0]): return 0
        numRows,  numColumns = len(grid), len(grid[0])
        count = 0


        def dfs(row, col):
            # edge cases
            if row < 0 or col < 0 or row>=numRows or col>=numColumns or grid[row][col]!='1': return
            # manipulate directly the input!! we can use extra space otherwise
            grid[row][col]='#'
            for dir in ((1,0), (-1,0), (0,1), (0,-1)):
                dfs(row+dir[0], col+dir[1])


        for row in range(numRows):
            for col in range(numColumns):
                if grid[row][col] == "1":
                    dfs(row, col)
                    count+=1

        return count


grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
print(Solution().numIslands(grid))

grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]

print(Solution().numIslands(grid))
