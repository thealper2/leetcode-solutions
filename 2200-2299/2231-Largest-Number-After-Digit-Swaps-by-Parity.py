class Solution:
    def largestInteger(self, num: int) -> int:
        n = 0
        odd = []
        even = []
        list_num = []

        while num > 0:
            d = num % 10
            num //= 10
            n += 1
            list_num.append(d)
            if d % 2 == 0:
                even.append(d)
            else:
                odd.append(d)

        odd.sort()
        even.sort()
        list_num = list_num[::-1]

        result = 0
        for i in range(n):
            if list_num[i] % 2 == 0:
                result = result * 10 + even.pop()
            else:
                result = result * 10 + odd.pop()

        return result