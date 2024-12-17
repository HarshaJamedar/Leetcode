class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if divisor != 0 and dividend >= -2**31 and dividend <= 2**31-1 :
            output = math.trunc(dividend/divisor)
        
        return min(output, 2**31-1)
        