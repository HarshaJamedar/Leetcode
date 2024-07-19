class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        def check(l,r):
            #checking for outofbounds and have same characters around the centre
            while l>=0 and r<len(s) and s[l] == s[r]:
                l -= 1
                r += 1
            #returning the palindrome between l and r by slicing
            return s[l+1:r]

        longest_palindrome = ""
        for i in range(len(s)):
            substring1 = check(i,i)
            if len(substring1) > len(longest_palindrome):
                longest_palindrome = substring1
            #when the length of substring is even need to increment i 
            substring2 = check(i,i+1)
            if len(substring2) > len(longest_palindrome):
                longest_palindrome = substring2
        return longest_palindrome

        