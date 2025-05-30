class Solution:
    def hasSpecialSubstring(self, s: str, k: int) -> bool:
        current_char = s[0]
        count = 1
        for char in s[1:]:
            if char == current_char:
                count += 1
            else:
                if count == k:
                    return True

                current_char = char
                count = 1
        
        return count == k
