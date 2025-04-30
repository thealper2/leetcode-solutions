from typing import List
from collections import defaultdict


class Solution:
    def shortestCompletingWord(self, licensePlate: str, words: List[str]) -> str:
        plate_count = defaultdict(int)
        for char in licensePlate.lower():
            if char.isalpha():
                plate_count[char] += 1
        
        shortest_word = None
        
        for word in words:
            word_count = defaultdict(int)
            for char in word.lower():
                word_count[char] += 1
            
            valid = True
            for char, count in plate_count.items():
                if word_count[char] < count:
                    valid = False
                    break
            
            if valid:
                if shortest_word is None or len(word) < len(shortest_word):
                    shortest_word = word
        
        return shortest_word