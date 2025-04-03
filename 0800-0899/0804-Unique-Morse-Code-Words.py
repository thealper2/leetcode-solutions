from typing import List


class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        result = []

        MORSE_CODE_DICT = {
            'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.',
            'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
            'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
            'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
            'Y': '-.--', 'Z': '--..',
        }

        for word in words:
            w = ""
            for c in word:
                w += MORSE_CODE_DICT[c.upper()]

            if w not in result:
                result.append(w)

        return len(result)