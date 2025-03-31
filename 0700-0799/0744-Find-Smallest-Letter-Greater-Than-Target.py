from typing import List


class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        smallest = None

        for letter in letters:
            if ord(letter) > ord(target):
                if smallest is None or ord(letter) < smallest:
                    smallest = ord(letter)

        return chr(smallest) if smallest is not None else letters[0]
