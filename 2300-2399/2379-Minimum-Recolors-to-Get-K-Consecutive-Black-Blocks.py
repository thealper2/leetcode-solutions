class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        n = len(blocks)
        min_operations = float('inf')
        window_white = 0
        
        for i in range(k):
            if blocks[i] == 'W':
                window_white += 1

        min_operations = window_white
        
        for i in range(k, n):
            if blocks[i - k] == 'W':
                window_white -= 1

            if blocks[i] == 'W':
                window_white += 1

            min_operations = min(min_operations, window_white)

            if min_operations == 0:
                return 0
        
        return min_operations