class Solution:
    def isPalindrome(self, x: int) -> bool:

        if x < 0:
            return False

        original = x
        prevNum = 0

        while x > 0:

            prevNum = (prevNum * 10) + x % 10

            x = x // 10

        return original == prevNum

    