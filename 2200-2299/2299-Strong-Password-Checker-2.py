class Solution:
    def strongPasswordCheckerII(self, password: str) -> bool:
        seen = set()

        for i, c in enumerate(password):
            if i > 0 and c == password[i - 1]:
                return False
            
            if c.isupper():
                seen.add(1)
            
            elif c.islower():
                seen.add(2)
            
            elif c.isdigit():
                seen.add(3)             
            
            else:
                seen.add(4)
        
        return len(password) > 7 and len(seen) == 4