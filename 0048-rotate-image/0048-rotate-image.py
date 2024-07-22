class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        left, right = 0, len(matrix)-1
        while left < right:
            for i in range(right-left):
                #initialize two more pointers as top and bottom
                top, bottom = left, right

                #save the top left and rotate the rows and columns
                top_left = matrix[top][left+i]

                #move bottom left to top left
                matrix[top][left+i] = matrix[bottom-i][left]

                #move bottom right to bottom left
                matrix[bottom-i][left] = matrix[bottom][right-i]

                #move top right to bottom right
                matrix[bottom][right-i] = matrix[top+i][right]

                #move top left to top right
                matrix[top+i][right] = top_left
            
            left += 1
            right -= 1
            


        