class Solution:
    def climbStairs(self, n: int) -> int:
        pattern = [0] * (n+1)
        pattern[0] = 1
        pattern[1] = 1

        for i in range(2, n+1):
            pattern[i] = pattern[i-1]+pattern[i-2]

        return pattern[-1]
        
        
        