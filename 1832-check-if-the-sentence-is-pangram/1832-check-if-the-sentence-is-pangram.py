class Solution(object):
    def checkIfPangram(self, sentence):
        """
        :type sentence: str
        :rtype: bool
        """
        a_set = set(sentence)
        
        return len(a_set) == 26