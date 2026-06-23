class Solution(object):
    def sortPeople(self, names, heights):
        """
        :type names: List[str]
        :type heights: List[int]
        :rtype: List[str]
        """
        mp = {}
        for i in range(len(names)):
            mp[heights[i]] = names[i]

        heights.sort(reverse=True)

        return [mp[h] for h in heights]
            
