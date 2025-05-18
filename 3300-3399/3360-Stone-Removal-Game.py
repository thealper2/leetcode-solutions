class Solution:
    def canAliceWin(self, n: int) -> bool:
        win = False
        remove = 10
        while n >= remove:
            n -= remove
            remove -= 1
            win = not win
            
        return win