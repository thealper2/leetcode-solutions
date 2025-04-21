class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        words = sentence.split()
        n = len(words)

        if n == 1:
            return words[0][0] == words[0][-1]
        
        for i in range(n - 1):
            if words[i][-1] != words[i+1][0]:
                return False
        
        return words[-1][-1] == words[0][0]