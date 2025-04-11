from typing import List


class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        common_counts = {}
        for char in words[0]:
            if char not in common_counts:
                common_counts[char] = 1
            else:
                common_counts[char] += 1

        for word in words[1:]:
            current_counts = {}
            for char in word:
                if char not in current_counts:
                    current_counts[char] = 1
                else:
                    current_counts[char] += 1


            for char in list(common_counts.keys()):
                if char in current_counts:
                    common_counts[char] = min(common_counts[char], current_counts[char])
                else:
                    del common_counts[char]
        
        result = []
        for char, count in common_counts.items():
            result.extend([char] * count)
        
        return result