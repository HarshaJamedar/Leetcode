class Solution:
    def reverse(self, x: int) -> int:
    
        if x < 0:
            sign = -1
        else:
            sign = 1
        string_x = str(x)
        reverse_x = ""
        n = len(string_x)-1
        while n >= 0:
            if string_x[n].isdigit():
                reverse_x += string_x[n]
            n -= 1
        x = sign*int(reverse_x)
        if x <= -2**31 or x >= 2**31 - 1:
            return 0
        else:
            return x

        