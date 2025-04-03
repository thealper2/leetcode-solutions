class Solution:
    def clearDigits(self, s: str) -> str:
        result = []
        for c in s:
            if c.isdigit():
                if result and not result[-1].isdigit():
                    result.pop()
            else:
                result.append(c)
        
        return "".join(result)