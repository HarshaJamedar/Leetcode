class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        #create a dictionary
        anagrams = {}
        for s in strs:
            sorted_str = ''.join(sorted(s))
            if sorted_str not in anagrams:
                #creating a key in a dictionary
                anagrams[sorted_str] = []
            anagrams[sorted_str].append(s)
        #returning all values to the keys in a list
        return list(anagrams.values())

        