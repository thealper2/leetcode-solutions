class Solution:
    def passwordStrength(self, password: str) -> int:
        unique = set(password)
        strength = 0
        for c in unique:
            if c.isalpha() and c.islower():
                strength += 1
            elif c.isalpha() and c.isupper():
                strength += 2
            elif c.isdigit():
                strength += 3
            else:
                strength += 5

        return strength