class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return "1"

        prev = self.countAndSay(n - 1)
        result = []
        i = 0
        l = len(prev)
        
        while i < l:
            curr = prev[i]
            count = 1
            while i + 1 < l and prev[i] == prev[i + 1]:
                count += 1
                i += 1

            result.append(f"{count}{curr}")
            i += 1
        
        return ''.join(result)
