class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def dfs(grid,i,j):
            if i <0 or i >= len(grid) or j <0 or j >= len(grid[0]):
                return
            for k in [[1,0],[0,1],[-1,0],[0,-1]]:
                if i + k[0] < 0 or i + k[0] >= len(grid) or j + k[1] <0 or j +k[1] >= len(grid[0]):
                    continue 
                if grid[i + k[0]][j + k[1]] == "1":
                    grid[i + k[0]][j + k[1]] = "0"
                    dfs(grid,i+k[0],j+k[1])
                # if grid[i + k[0]][j + k[1]] == "1":
                #     grid[i + k[0]][j + k[1]] == "0"
                #     dfs(grid,i + k[0],j + k[1])
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    # print(i,j)
                    dfs(grid,i,j)
                    count += 1
        return count

# class Solution:
#     def numIslands(self, grid: List[List[str]]) -> int:
#         def dfs(grid: List[List[str]],i,j):
#             if i <0 or i >= len(grid) or j <0 or j >= len(grid[0]):
#                 return
#             for k in [[1,0],[0,1],[-1,0],[0,-1]]:
                
#                 if i + k[0] < 0 or i + k[0] >= len(grid) or j + k[1] <0 or j +k[1] >= len(grid[0]):
#                     continue 
#                 if grid[i + k[0]][j + k[1]] == "1":
#                     grid[i + k[0]][j + k[1]] = "0"
#                     dfs(grid,i+k[0],j+k[1])
                
#         count = 0
#         for i in range(len(grid)):
#             for j in range(len(grid[0])):
#                 if grid[i][j] == "1":
#                     # print(i,j)
#                     dfs(grid,i,j)
#                     count += 1
#         return count