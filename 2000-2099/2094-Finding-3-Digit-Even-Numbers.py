from typing import List
from itertools import permutations

class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        unique_numbers = set()
        for triplet in permutations(digits, 3):
            if triplet[0] != 0 and triplet[2] % 2 == 0:
                number = triplet[0] * 100 + triplet[1] * 10 + triplet[2]
                unique_numbers.add(number)

        return sorted(unique_numbers)