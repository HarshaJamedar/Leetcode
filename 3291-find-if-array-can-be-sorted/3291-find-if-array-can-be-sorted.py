class Solution:
    def canSortArray(self, nums: List[int]) -> bool:
        prevMax, currMin, currMax = 0, 0, 0
        prevBit = -1
        for num in nums:
            b = num.bit_count()
            if prevBit != b:
                if currMin < prevMax:
                    return False
                prevMax = currMax
                currMin, currMax = num, num
                prevBit = b
            else:
                currMin = min(currMin, num)
                currMax = max(currMax, num)
        return currMin >= prevMax
        