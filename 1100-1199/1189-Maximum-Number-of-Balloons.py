class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        letters = {
            'b': 0,
            'a': 0,
            'l': 0,
            'o': 0,
            'n': 0
        }
        for c in text:
            if c in letters:
                letters[c] += 1

        count = 0
        while True:
            for x in 'balloon':
                letters[x] -= 1
                if letters[x] < 0:
                    return count
                
            count += 1

        return count