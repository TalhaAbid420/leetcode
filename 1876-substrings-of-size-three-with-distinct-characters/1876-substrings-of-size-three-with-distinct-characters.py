class Solution(object):
    def countGoodSubstrings(self, s):
        
        left = 0
        ans = 0

        for right in range(len(s)):

            if right - left + 1 == 3:

                if len(set(s[left:right+1])) == 3:

                    ans += 1

                left += 1

        return ans