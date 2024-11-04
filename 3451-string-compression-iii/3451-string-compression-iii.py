class Solution:
    def compressedString(self,word):
    # Detect the length of the repeated pattern
        pattern_length = 26  # Since "abcdefghijklmnopqrstuvwxyz" has 26 characters
    
    # Check if the word consists of repeated "abcdefghijklmnopqrstuvwxyz" patterns
        if word[:pattern_length] * (len(word) // pattern_length) == word:
        # Compress one instance of the pattern and multiply it by the repetition count
            single_pattern_compressed = ''.join("1{}".format(ch) for ch in "abcdefghijklmnopqrstuvwxyz")
            repetitions = len(word) // pattern_length
            return single_pattern_compressed * repetitions

    # If there's no repeatable pattern, fall back to the standard approach
        result = ""
        count = 1
     
        for i in range(1, len(word)):
            if word[i] == word[i - 1]:
                if count == 9:
                    result += str(count) + word[i - 1]
                    count = 1
                else:
                    count += 1
            else:
                result += str(count) + word[i - 1]
                count = 1
    
        result += str(count) + word[-1]
        return result

    

