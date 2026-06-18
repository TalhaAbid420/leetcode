class Solution(object):
    def rotateString(self, s, goal):

        if len(s) != len(goal):
            return False

        s_list = list(s)

        for _ in range(len(s)):
            
            if "".join(s_list) == goal:
                return True

            first_char = s_list.pop(0)

            s_list.append(first_char)

        return False


        