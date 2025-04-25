class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        sentence = sentence.split()
        n = len(sentence)
        for i in range(n):
            if sentence[i].startswith(searchWord):
                return i + 1
            
        return -1