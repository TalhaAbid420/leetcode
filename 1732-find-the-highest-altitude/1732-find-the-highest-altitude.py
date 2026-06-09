class Solution(object):
    def largestAltitude(self, gain):
        
        prev = 0
        new_arr = [0]
        for i in range(prev, len(gain)):
            prev = prev + gain[i]
            new_arr.append(prev)
        
        return max(new_arr)