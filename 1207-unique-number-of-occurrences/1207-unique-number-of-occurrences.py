class Solution(object):
    def uniqueOccurrences(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        freq = {}

        for num in arr:
            freq[num] = freq.get(num, 0) + 1

        seen = set()

        for count in freq.values():
            if count in seen:
                return False
            seen.add(count)
        
        return True
        