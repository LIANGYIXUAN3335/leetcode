class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = collections.defaultdict(list)
## collections.defaultdict(type of value)  in comman sence ,we can not set only value type with out key, but defaultdict
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord("a")] += 1
## list is not hashable , we need to change list to tuple then we make it a key
            ans[tuple(count)].append(s)
        return ans.values()