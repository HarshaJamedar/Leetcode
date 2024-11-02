class Solution(object):
    def isCircularSentence(self, sentence):
        words = sentence.split()
        if len(words) == 1:
            return words[0][0] == words[0][-1]
        elif words[0][0] != words[-1][-1]:
            return False
        else:
            for i in range(len(words) - 1):
                if words[i][-1] != words[i + 1][0]:
                    return False
            return True
        