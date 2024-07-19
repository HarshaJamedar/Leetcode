class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        def search_first(nums,target,n):
            left = 0
            right = n-1
            first = -1
            while left<= right :
                mid = (left+right)//2
                if nums[mid] == target:
                    first = mid
                    right = mid-1
                elif nums[mid] > target:
                    right = mid-1
                else:
                    left = mid+1
            return first

        def search_last(nums,target,n):
            left = 0
            right = n-1
            last = -1
            while left <= right:
                mid = (left+right)//2
                if nums[mid]== target:
                    last = mid
                    left = mid+1
                elif nums[mid] > target:
                    right = mid-1
                else:
                    left = mid+1
            return last
                    


    
        res = []
        n= len(nums)
        first = search_first(nums, target, n)
        last = search_last(nums, target, n)
        res.append(first)
        res.append(last)
        return res
         