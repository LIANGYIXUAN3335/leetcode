class Solution:
    def countBits(self, n: int) -> List[int]:
#  1 - 00000001
#  2 - 00000010
#  3 - 00000011
#  4 - 00000100
        i, iteration = 2, 2
        ans = [0] * (n + 3) 
        ans[0] = 0 
        ans[1] = 1
        while i <= n:
            end = min(n + 1,i + iteration)
            for index in range(i, end):
                ans[index] = 1 + ans[index - iteration]
            i =  end
            iteration *= 2
        return ans[0 : n + 1]