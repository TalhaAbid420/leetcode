class Solution(object):
    def checkIfPangram(self, sentence):
        """
        :type sentence: str
        :rtype: bool
        """
        a_set = set()
        for char in sentence:
            a_set.add(char)
        
        return len(a_set) == 26