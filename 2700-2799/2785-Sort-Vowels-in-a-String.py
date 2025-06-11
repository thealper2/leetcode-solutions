class Solution:
    def sortVowels(self, s: str) -> str:
        vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
        s_list = list(s)
        vowel_indices = []
        vowel_chars = []
        
        for i, char in enumerate(s_list):
            if char in vowels:
                vowel_indices.append(i)
                vowel_chars.append(char)
        
        vowel_chars.sort(key=lambda x: ord(x))
        
        for idx, vowel in zip(vowel_indices, vowel_chars):
            s_list[idx] = vowel
        
        return ''.join(s_list)
