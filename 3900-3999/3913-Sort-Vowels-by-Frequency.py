class Solution:
    def sortVowels(self, s: str) -> str:
        vowels = {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}
        s = list(s)
        vowel_indices = []
        vowel_chars = []

        for i, c in enumerate(s):
            if c in vowels:
                vowel_indices.append(i)
                vowel_chars.append(c)

        freq = {}
        for v in vowel_chars:
            freq[v] = freq.get(v, 0) + 1

        first_occurrence = {}
        for v in vowel_chars:
            if v not in first_occurrence:
                first_occurrence[v] = vowel_indices[vowel_chars.index(v)]
        
        vowel_chars.sort(key=lambda x: (-freq[x], first_occurrence[x]))

        for idx, vowel in zip(vowel_indices, vowel_chars):
            s[idx] = vowel

        return ''.join(s)