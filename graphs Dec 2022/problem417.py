class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        pacific = set()
        atlantic  = set()
        row = len(heights)
        col = len(heights[0])
        def dfs(visit,i,j,preheight):
            if (i,j) in visit or heights[i][j] < preheight:
                return
            visit.add((i,j))
            for k in [[1,0],[0,1],[-1,0],[0,-1]]:
                if i + k[0] in range(row) and j + k[1] in range(col):
                    dfs(visit,i + k[0] , j + k[1], heights[i][j])
        for i in range(row):
            dfs(pacific,i,0,heights[i][0])
            dfs(atlantic,i,col - 1,heights[i][col - 1])
        for j in range(col):
            dfs(pacific,0,j,heights[0][j])
            dfs(atlantic,row - 1,j,heights[row - 1][j])
        ans = []
        for m in range(row):
            for n in range(col):
                if (m,n) in pacific and (m,n) in atlantic:
                    ans.append((m,n))
        return ans