class Solution:
    def areNumbersAscending(self, s: str) -> bool:
        l = None
        for word in s.split():
            if word.isdigit():
                if not l:
                    l = int(word)
                else:
                    if l < int(word):
                        l = int(word)
                    else:
                        return False
        
        return True