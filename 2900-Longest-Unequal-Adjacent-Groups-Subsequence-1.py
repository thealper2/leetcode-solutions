class Solution:
    def getLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:
        result = [words[0]]
        prev = groups[0]

        for i in range(1, len(words)):
            if groups[i] != prev:
                result.append(words[i])

            prev = groups[i]

        return result


###


class Solution2:
    def getLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:
        result = [words[0]]
        for i in range(1, len(words)):
            if groups[i] != groups[i - 1]:
                result.append(words[i])

        return result
