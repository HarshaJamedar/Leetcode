class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        trimmed_str = ""
        for char in s:
            if char.isalnum():
                trimmed_str += ''.join(char.lower())
        return trimmed_str == trimmed_str[::-1]


        