class Solution:
    def sortSentence(self, s: str) -> str:
        result = [""] * len(s.split(" "))
        for word in s.split(" "):
            idx = word[-1]
            result[int(idx) - 1] = word[:-1]

        return " ".join(result)
