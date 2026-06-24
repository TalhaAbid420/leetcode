class Solution:
    def majorityElement(self, nums):
        
        freq = {}

        for num in nums:
            freq[num] = freq.get(num, 0) + 1

        limit = len(nums) // 2

        for num, count in freq.items():
            if count > limit:
                return num
