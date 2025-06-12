from typing import List


class Solution:
    def pattern_code_generator(self, word):
        pattern_code = ""
        unique_chars = set()
        masked = {}
        n = len(word)
        idx = 65

        for i in range(n):
            if word[i] not in unique_chars:
                unique_chars.add(word[i])
                char_idx = chr(idx)
                masked[word[i]] = char_idx
                idx += 1
                pattern_code += masked[word[i]]
            else:
                pattern_code += masked[word[i]]
                
        return pattern_code

    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        patterns_code = self.pattern_code_generator(pattern)
        result = []

        for word in words:
            if self.pattern_code_generator(word) == patterns_code:
                result.append(word)

        return result
