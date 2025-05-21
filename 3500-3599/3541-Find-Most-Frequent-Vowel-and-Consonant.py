class Solution:
    def maxFreqSum(self, s: str) -> int:
        counts = {}
        vowels = {'a', 'e', 'i', 'o', 'u'}
        max_vowel, max_consonant = 0, 0

        for c in s:
            if c not in counts:
                counts[c] = 1
            else:
                counts[c] += 1

            if c in vowels:
                if counts[c] > max_vowel:
                    max_vowel = counts[c]
            else:
                if counts[c] > max_consonant:
                    max_consonant = counts[c]

        return max_vowel + max_consonant
