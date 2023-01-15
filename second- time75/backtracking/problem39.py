class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        def dfs(index,cursum):
            if cursum ==  target:
                res.append(cur.copy())
                return
            elif cursum > target:
                return
            for i in range(index, len(candidates)):
                print(index, cur)
                cur.append(candidates[i])
                dfs(i, cursum + candidates[i])
                cur.pop()
        cur = []
        dfs(0, 0)
        return res