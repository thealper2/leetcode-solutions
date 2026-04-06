class Solution:
    def doesAliceWin(self, s: str) -> bool:
        vowels = 'aeiou'
        count = 0
        for c in s:
            if c.lower() in vowels:
                count += 1

        if count  == 0:
            return False

        if count % 2 == 1:
            return True

        return True if count > 0 else False

