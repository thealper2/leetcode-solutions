from typing import List
import re
from collections import defaultdict

class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        banned = set(banned)
        words = re.findall(r'\w+', paragraph.lower())
        words = [word for word in words if word not in banned]
        
        word_counts = defaultdict(int)
        max_count = 0
        result = ""
        
        for word in words:
            word_counts[word] += 1
            if word_counts[word] > max_count:
                max_count = word_counts[word]
                result = word
        
        return result