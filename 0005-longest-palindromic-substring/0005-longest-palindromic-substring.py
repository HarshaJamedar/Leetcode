class Solution:
    def longestPalindrome(self, s: str) -> str:
        def expand(l,r):
            while l>=0 and r<len(s) and s[l] == s[r]:
                l -= 1
                r += 1
            return s[l+1:r]

        result = ""
        for i in range(len(s)):
            substring1 = expand(i,i)
            if len(substring1) > len(result):
                result = substring1
            substring2 = expand(i, i+1)
            if len(substring2) > len(result):
                result = substring2
        return result
        
        