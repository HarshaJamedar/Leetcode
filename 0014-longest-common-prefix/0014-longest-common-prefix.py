class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        res = ""
        if len(strs) == 0: return ""
        strs.sort()
        for i in range(len(strs[0])):
            if strs[0][i] != strs[-1][i]:
                break
            res += "".join(strs[0][i])
        return res

        
        