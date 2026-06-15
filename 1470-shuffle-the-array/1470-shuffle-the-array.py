class Solution(object):
    def shuffle(self, nums, n):
        
        left = 0
        right = n
        result = []

        while left < n:
            result.append(nums[left])
            result.append(nums[right])
            left += 1
            right += 1

        return result