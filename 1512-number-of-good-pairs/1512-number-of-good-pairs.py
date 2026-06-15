class Solution(object):
    def numIdenticalPairs(self, nums):
        count = 0
        seen = Counter()

        for num in nums:

            count += seen[num]

            seen[num] += 1

        return count