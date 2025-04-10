class Solution:
    def getLucky(self, s: str, k: int) -> int:
        num_str = ''
        for char in s:
            num = ord(char) - ord('a') + 1
            num_str += str(num)
        
        num = int(num_str)

        for _ in range(k):
            x = 0
            while num > 0:
                x += num % 10
                num //= 10
            
            num = x

        return num