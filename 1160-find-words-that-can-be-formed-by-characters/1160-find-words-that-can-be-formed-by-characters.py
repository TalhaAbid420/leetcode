class Solution(object):
    def countCharacters(self, words, chars):
        chars_count = Counter(chars)
        total_len = 0

        for word in words:
            words_count = Counter(word)
            can_form = True

            for char, count in words_count.items():
                if chars_count[char] < count:
                    can_form = False
                    break
            if can_form:
                total_len += len(word)

        return total_len