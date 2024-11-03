class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        hashMap = {}
        max_length = 0
        left = 0
        for right in range(len(s)):
            if s[right] in hashMap:
                left = max(left,hashMap[s[right]]+1)
            hashMap[s[right]] = right
            max_length = max(max_length, right-left+1)
        return max_length 
        
        
        

        