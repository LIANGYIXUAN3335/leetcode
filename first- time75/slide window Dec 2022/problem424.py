class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        LetterFrequency = {}
        maxSameLetter = 0
        l = 0 
        for r in range(len(s)):
            LetterFrequency[s[r]] = LetterFrequency.get(s[r] , 0) + 1
            # check if valid
            if r - l + 1 - max(LetterFrequency.values()) <= k:
                maxSameLetter = max(maxSameLetter, r - l +1)
                
            elif r - l + 1 - max(LetterFrequency.values()) > k:
                LetterFrequency[s[l]] =  LetterFrequency.get(s[l]) - 1
                l += 1      
        return maxSameLetter
        