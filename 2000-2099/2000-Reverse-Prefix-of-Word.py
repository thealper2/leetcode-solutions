class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        idx = 0
        for i in range(len(word)):
            if word[i] == ch:
                idx = i
                break

        if idx == 0:
            return word
        else:
            return word[:idx+1][::-1] + word[idx+1:]