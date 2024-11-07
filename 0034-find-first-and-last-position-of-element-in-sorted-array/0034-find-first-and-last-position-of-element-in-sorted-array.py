class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if target not in nums:
            return [-1,-1]

        left = self.binarySearch(nums, target, 0)
        right = self.binarySearch(nums, target, 1)
        return [left,right]

        
    def binarySearch(self, nums: List[int], target: int, pos: int):
        left , right = 0, len(nums)-1
        index = -1
        while left<=right:
            mid = (left+right)//2
            if target > nums[mid]:
                left = mid+1
            elif target < nums[mid]:
                right = mid-1
            else:
                index = mid
                if pos == 0:
                    right = mid-1
                else:
                    left = mid+1
        return index
        
            


        