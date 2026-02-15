class Solution:
    def reverseByType(self, s: str) -> str:
        chars = list(s)
        letters = [c for c in chars if c.islower()]
        specials = [c for c in chars if not c.islower()]
        letters.reverse()
        specials.reverse()
        result = []
        for c in chars:
            if c.islower():
                result.append(letters.pop(0))
            else:
                result.append(specials.pop(0))

        return "".join(result)
