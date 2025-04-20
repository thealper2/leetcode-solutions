class Solution:
    def greatestLetter(self, s: str) -> str:
        seen = set()
        result = ''

        for c in s:
            if c.islower():
                upper = c.upper()
                if upper in seen:
                    if upper > result:
                        result = upper

            else:
                lower = c.lower()
                if lower in seen:
                    if c > result:
                        result = c

            seen.add(c)

        return result