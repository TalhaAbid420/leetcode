class Solution:
    def isPalindrome(self, x: int) -> bool:

        original = x
        prevNum = 0

        while x > 0:

            lastdigit = x % 10

            prevNum = (prevNum * 10) + lastdigit

            x = x // 10

        return original == prevNum

    