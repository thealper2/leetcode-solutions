class Solution:
    def maxRepeating(self, sequence: str, word: str) -> int:
        times = 0
        max_times = len(sequence) // len(word)
        for i in range(1, max_times + 1):
            search = word * i
            n = len(search)
            for j in range(0, len(sequence)):
                if sequence[j:j+n] == search:
                    times += 1
                    break

        return times