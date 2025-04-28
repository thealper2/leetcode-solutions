class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        found = False
        result = 0

        while not found:
            product = 1
            temp = n

            while temp > 0:
                product *= temp % 10
                temp //= 10

            if product % t == 0:
                result = n
                found = True
            else:
                n += 1

        return result