class Solution:
    def percentageLetter(s: str, letter: str) -> int:
        count = 0
        for c in s:
            if c == letter:
                count += 1
        
        total = len(s)
        if total == 0:
            return 0
        percentage = (count * 100) // total
        return percentage