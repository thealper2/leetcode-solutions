from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        digits_to_letters = {
            '2': ['a', 'b', 'c'],
            '3': ['d', 'e', 'f'],
            '4': ['g', 'h', 'i'],
            '5': ['j', 'k', 'l'],
            '6': ['m', 'n', 'o'],
            '7': ['p', 'q', 'r', 's'],
            '8': ['t', 'u', 'v'],
            '9': ['w', 'x', 'y', 'z']
        }

        combinations = ['']

        for digit in digits:
            current_letters = digits_to_letters[digit]
            new_combinations = []
            for combination in combinations:
                for letter in current_letters:
                    new_combinations.append(combination + letter)
        
            combinations = new_combinations

        return combinations