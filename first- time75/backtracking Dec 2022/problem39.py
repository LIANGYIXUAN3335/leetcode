class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        # reverse =  True means ascending and False means descending
        candidates.sort(reverse = False)
        def dfs(pre,candidates,index):
            for i in range(index,len(candidates)):
                # print(res)
                print(pre)
                curtotal = candidates[i] + sum(pre)
                if curtotal ==  target:
                    pre.append(candidates[i])
                    res.append(pre.copy())
                    pre.pop()
                    return
                elif curtotal > target:
                    return
                else:
                    pre.append(candidates[i])
                    dfs(pre, candidates,i)
                    pre.pop()
        dfs([],candidates,0)
        return res