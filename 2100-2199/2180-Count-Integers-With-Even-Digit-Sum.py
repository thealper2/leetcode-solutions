class Solution:
    def countEven(self, num: int) -> int:
        c = 0
        
        for i in range(1, num + 1):
            t = 0
            i = str(i)
            for char in i:
                t += int(char)

            if t % 2 == 0:
                c += 1

        return c