class Solution:
    def winningPlayer(self, x: int, y: int) -> str:
        moves = 0
        while x >= 1 and y >= 4:
            x -= 1
            y -= 4
            moves += 1
        
        if moves % 2 == 1:
            return "Alice"

        return "Bob"