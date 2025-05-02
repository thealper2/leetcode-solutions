class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        last = None

        while n >= 1:
            d = n % 2
            n //= 2
            if last == None:
                last = d
            else:
                if d == last:
                    return False
                
                last = d

        return True