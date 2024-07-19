class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(len(nums)):
            temp = target-nums[i]
            nums[i]='inf'
            if temp in nums:
                return [i,(nums.index(temp))]
        



        

        