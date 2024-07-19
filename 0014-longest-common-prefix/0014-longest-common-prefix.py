class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        res = ""
        if len(strs) == 0: return ""
        strs.sort()
        first = strs[0]
        last = strs[-1]
        for i in range(len(first)):
            if first[i] != last[i]:
                break
            res += "".join(first[i])
        return res

        
        