class Solution:
    def toGoatLatin(self, sentence: str) -> str:
        sentence = sentence.split()
        n = len(sentence)
        vowels = {'a', 'e', 'i', 'o', 'u'}

        for i in range(n):
            if sentence[i][0].lower() in vowels:
                sentence[i] = sentence[i] + "m" + "a" * (i + 2)
            else:
                sentence[i] = sentence[i][1:] + sentence[i][0] + "m" + "a"  *(i + 2)

        return ' '.join(sentence)