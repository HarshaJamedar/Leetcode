class Solution:
    def isPalindrome(self, x: int) -> bool:
        numbers = str(x)
        rev_numbers = numbers[::-1]
        if numbers == rev_numbers:
            return True
        return False

        