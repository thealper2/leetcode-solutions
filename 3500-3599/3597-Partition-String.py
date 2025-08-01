from typing import List


class Solution:
    def partitionString(self, s: str) -> List[str]:
        segments = []
        seen = set()
        current_segment = ""
        
        for char in s:
            current_segment += char
            if current_segment not in seen:
                segments.append(current_segment)
                seen.add(current_segment)
                current_segment = ""
        
        return segments
