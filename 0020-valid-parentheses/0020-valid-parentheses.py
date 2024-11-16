class Solution:
    def isValid(self, s: str) -> bool:
        Dictionary = {")":"(", "}":"{","]":"["}
        stack = []
        for bracket in s:
            if bracket in Dictionary.values():
                stack.append(bracket)
            elif bracket in Dictionary.keys():
                if not stack or Dictionary[bracket] != stack.pop():
                    return False
        return not stack
            
        


        