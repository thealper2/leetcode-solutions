from typing import List


class Solution:
    def oddString(self, words: List[str]) -> str:
        result = []
        diff_dict = {}

        for word in words:
            temp = []
            for i in range(len(word) - 1):
                temp.append(ord(word[i + 1]) - ord(word[i]))

            diff_dict[str(temp)] = word

            if temp not in result:
                result.append(temp)
            else:
                result.remove(temp)

        return diff_dict[str(result[0])]