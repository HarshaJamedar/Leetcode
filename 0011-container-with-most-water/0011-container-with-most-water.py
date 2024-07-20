class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        n = len(height)
        l=0
        r=n-1
        min_height = max(height)
        max_capacity = 0
        while l<r:
            width = r-l
            min_height = min(height[l],height[r])
            current_area = min_height * width
            max_capacity = max(max_capacity,current_area)

            if(height[l] < height[r]):
                l += 1
            else:
                r -= 1
        return max_capacity





        