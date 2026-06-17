class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        
        count = 0
        max_count = 0

        for num in nums:

            if num:
                count += 1
            else:
                if count > max_count:
                    max_count = count
                count = 0

        return count if count > max_count else max_count