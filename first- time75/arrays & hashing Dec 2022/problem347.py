class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic = {}
        # we have to make i in range(len(nums) + 1) otherwise we may out of index
        frequency = [[] for i in range(len(nums) +1)]
        for i in nums:
            dic[i] = dic.get(i,0) +1
        for key, value in dic.items():
            frequency[value].append(key)
        res = []
        for i in range(len(frequency) -1 , 0, -1):
            for j in frequency[i]:
                res.append(j)
            k -= len(frequency[i])
            if k == 0:
                return res