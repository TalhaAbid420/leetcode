class Solution(object):
    def findIntersectionValues(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        set1 = set(nums1)
        set2 = set(nums2)

        ans1 = 0
        ans2 = 0

        for i in nums1:
            if i in set2:
                ans1 += 1

        for i in nums2:
            if i in set1:
                ans2 += 1

        return [ans1, ans2]
        
        