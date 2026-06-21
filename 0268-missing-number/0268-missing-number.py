class Solution(object):
    def missingNumber(self, nums):
        n = len(nums)
        nums_set = set(nums)
        

        for i in range(n + 1):
            if i not in nums_set:
                return i

        
        return len(nums)