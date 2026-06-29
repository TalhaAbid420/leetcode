class Solution(object):
    def mergeAlternately(self, word1, word2):
        
        a = 0
        b = 0

        result = []

        while a < len(word1) and b < len(word2):
            result.append(word1[a])
            result.append(word2[b])
            a += 1
            b += 1

        while a < len(word1):
            result.append(word1[a])
            a += 1

        while b < len(word2):
            result.append(word2[b])
            b += 1

        return "".join(result)
        