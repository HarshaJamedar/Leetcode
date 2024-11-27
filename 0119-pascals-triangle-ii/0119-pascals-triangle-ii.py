class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        result = [1]
        prev = 1
        for i in range(1,rowIndex + 1):
            temp = prev * (rowIndex - i + 1) // i
            result.append(temp)
            prev = temp
        return result

        

        