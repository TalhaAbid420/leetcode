class Solution(object):
    def reverseVowels(self, s):
        s_list = list(s)
        vowels = set("aeiouAEIOU")
        left = 0
        right = len(s) - 1
        
        while left < right:
            if s_list[left] not in vowels:
                left += 1  # Skip left non-vowel
            elif s_list[right] not in vowels:
                right -= 1  # Skip right non-vowel
            else:
                # Both are vowels, so swap them
                s_list[left], s_list[right] = s_list[right], s_list[left]
                left += 1
                right -= 1
                
        return "".join(s_list)
