from collections import defaultdict
from typing import List

class Solution:
    def findCommonResponse(self, responses: List[List[str]]) -> str:
        count = defaultdict(int)

        for daily in responses:
            unique_responses = set(daily)
            for response in unique_responses:
                count[response] += 1

        max_freq = -1
        result = ""

        for response, freq in count.items():
            if freq > max_freq:
                max_freq = freq
                result = response
            elif freq == max_freq and response < result:
                result = response

        return result
