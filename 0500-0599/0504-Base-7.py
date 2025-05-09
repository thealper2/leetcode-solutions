class Solution:
    def convertToBase7(self, num: int) -> str:
        if num == 0:
            return '0'
        
        base = []
        temp = abs(num)
        a = ''
        if num < 0:
            a = '-'

        while temp > 0:
            base.append(str(temp % 7))
            temp //= 7

        return a + ''.join(base[::-1])