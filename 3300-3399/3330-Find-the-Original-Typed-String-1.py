class Solution:
    def possibleStringCount(self, word: str) -> int:
        count = 1
        n = len(word)
        for i in range(1, n):
            if word[i] == word[i - 1]:
                count += 1

        return count
        