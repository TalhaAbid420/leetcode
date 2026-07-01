class Solution(object):
    def sortArrayByParity(self, nums):
        

        even = []
        odd = []

        for num in nums:
            if num % 2 == 0:
                even.append(num)

            if num % 2 == 1:
                odd.append(num)

        return even  + odd