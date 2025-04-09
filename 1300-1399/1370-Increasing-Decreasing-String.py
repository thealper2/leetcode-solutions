class Solution:
    def sortString(self, s: str) -> str:
        freq = {}
        for char in s:
            if char not in freq:
                freq[char] = 1
            else:
                freq[char] += 1
        
        sorted_chars = sorted(freq.keys())
        result = []
        total_chars = len(s)

        while len(result) < total_chars:
            for char in sorted_chars:
                if freq[char] > 0:
                    result.append(char)
                    freq[char] -= 1

            for char in reversed(sorted_chars):
                if freq[char] > 0:
                    result.append(char)
                    freq[char] -= 1
                    
        return ''.join(result)