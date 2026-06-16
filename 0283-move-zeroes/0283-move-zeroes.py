class Solution(object):
    def moveZeroes(self, nums):
        
        insert_pos = 0
    
        # Step 1: Shift non-zero elements forward
        for num in nums:
            if num != 0:
                nums[insert_pos] = num
                insert_pos += 1
                
        # Step 2: Fill the rest of the array with zeroes
        for i in range(insert_pos, len(nums)):
            nums[i] = 0
        