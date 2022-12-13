class Solution(object):
    def containsDuplicate(self, nums):
        map = set()
        for i in nums:
            if i in map:
                return True
            else:
                map.add(i)
        return False
        """
        :type nums: List[int]
        :rtype: bool
        """