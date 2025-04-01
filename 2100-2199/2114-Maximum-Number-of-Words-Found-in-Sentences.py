from typing import List


class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        max_len = 0

        for sentence in sentences:
            if len(sentence.split(" ")) > max_len:
                max_len = len(sentence.split(" "))

        return max_len