class Solution(object):
    def countGoodSubstrings(self, s):
        ans = 0
        
        for i in range(len(s) - 2):
            substring = s[i: i+3]

            if len(set(substring)) == 3:
                ans += 1

        return ans
        