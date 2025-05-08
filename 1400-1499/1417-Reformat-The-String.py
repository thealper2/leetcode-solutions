class Solution:
    def reformat(self, s: str) -> str:
        digits = []
        letters = []
        c_digits = 0
        c_letters = 0

        for c in s:
            if c.isdigit():
                digits.append(c)
                c_digits += 1
            else:
                letters.append(c)
                c_letters += 1

        if abs(c_digits - c_letters) > 1:
            return ''
        
        result = []
        first = 0
        # 1: digit first, 0: letter first
        if c_letters < c_digits:
            first = 1

        while digits or letters:
            if first:
                result.append(digits.pop())
            else:
                result.append(letters.pop())

            first = not first

        return ''.join(result)