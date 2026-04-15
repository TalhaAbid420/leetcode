class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        nums_with_index = [(num, i) for i, num in enumerate(nums)]

        nums_with_index.sort()

        left = 0
        right = len(nums) - 1

        while left < right:
            curr_sum = nums_with_index[left][0] + nums_with_index[right][0]

            if curr_sum == target:

                return [nums_with_index[left][1], nums_with_index[right][1]]

            elif curr_sum > target:
                right -= 1

            else:
                left += 1

