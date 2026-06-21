class Solution(object):
    def sortString(self, s):
        """
        :type s: str
        :rtype: str
        """
        s_count = Counter(s)
        res = []
        total_len = len(s)

        unique_char = sorted(s_count.keys())

        while len(res) < total_len:
            for char in unique_char:
                if s_count[char] > 0:
                    res.append(char)
                    s_count[char] -= 1

            for char in reversed(unique_char):
                if s_count[char] > 0:
                    res.append(char)
                    s_count[char] -= 1

        return "".join(res)
        