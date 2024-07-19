class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        l = 0
        longest = 0
        unique_letters = set()

        for r in range(len(s)):
            #if the char is in set, we have to remove the char in set before moving l to next index
            while s[r] in unique_letters:
                unique_letters.remove(s[l])
                l += 1
            #window gives the substring length using sliding window technique
            window = (r-l)+1
            longest = max(longest,window)
            unique_letters.add(s[r])
        return longest


        