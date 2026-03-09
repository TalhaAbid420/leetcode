class Solution:
    def sortString(self, s: str) -> str:
        s = list(s)
        result = []

        while len(s) > 0:
            for i in sorted(set(s)):
                result.append(i)
                s.remove(i)
            for i in sorted(set(s), reverse=True):
                result.append(i)
                s.remove(i)
            
        return "".join(result)