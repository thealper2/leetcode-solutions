from typing import List


class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        count = 0
        rules = {"type": 0, "color": 1, "name": 2}

        for item in items:
            if item[rules[ruleKey]] == ruleValue:
                count += 1

        return count