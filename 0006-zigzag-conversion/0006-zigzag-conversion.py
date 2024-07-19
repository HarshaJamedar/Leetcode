class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1:
            return s
        zigzag = ""
        for row in range(numRows):
            step = 2*(numRows-1)
            for i in range(row, len(s), step):
                #for index 0 at p and nxt char at step 2*(numRows-1)th
                zigzag += s[i]
                #row in bounds and for each increasing row 
                # we noticed the step size decrease by 2*i
                #i.e i+step - 2*row
                if (row > 0 and row < numRows-1 and (i+step-(2*row)) < len(s)):
                    zigzag += s[i+step-(2*row)]
        return zigzag
        
                




        