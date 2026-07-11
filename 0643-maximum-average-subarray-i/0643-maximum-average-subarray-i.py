class Solution:
    def findMaxAverage(self, nums, k):

        window_sum = sum(nums[:k])
        max_sum = window_sum

        left = 0

        for right in range(k, len(nums)):
            window_sum = window_sum - nums[left] + nums[right]
            left += 1
            max_sum = max(max_sum, window_sum)

        return max_sum / k