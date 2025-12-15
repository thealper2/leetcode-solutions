class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split()
        if not words:
            return ""

        count_vowels = lambda x: sum(1 for c in x if c in 'aeiou')
        first_vowel = count_vowels(words[0])

        result = [words[0]]
        for word in words[1:]:
            if count_vowels(word) == first_vowel:
                result.append(word[::-1])
            else:
                result.append(word)

        return ' '.join(result)
