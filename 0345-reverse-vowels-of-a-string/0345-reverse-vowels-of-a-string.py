class Solution(object):
    def reverseVowels(self, s):

        s_list = list(s)

        vowels = set("aeiouAEIOU")

        left = 0
        right = len(s)-1

        while left < right:
            while left < right and s[left] not in vowels:
                left += 1
            while left < right and s[right] not in vowels:
                right -= 1

            s_list[left], s_list[right] = s_list[right], s_list[left]

            left += 1
            right -= 1

        return "".join(s_list)

