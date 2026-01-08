class Solution:
    def largestEven(self, s: str) -> str:
        idx = s.rfind('2')
        return s[:idx + 1] if idx != -1 else ""
