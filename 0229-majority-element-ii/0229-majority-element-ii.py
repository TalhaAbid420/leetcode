class Solution:
    def majorityElement(self, nums):
        freq = {}
        
        for num in nums:
            freq[num] = freq.get(num, 0) + 1

        limit = len(nums) // 3
        result = []

        for num, count in freq.items():
            if count > limit:
                result.append(num)

        return result