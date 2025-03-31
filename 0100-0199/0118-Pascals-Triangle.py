class Solution:
    def factorial(n):
        if n == 0:
            return 1
        else:
            return n * factorial(n - 1)

    def generate(self, numRows: int) -> List[List[int]]:
        result = []
        for i in range(numRows):
            temp = []
            for j in range(i + 1):
                if j == 0 or j == i:
                    temp.append(1)
                else:
                    temp.append(factorial(i) // (factorial(j) * factorial(i - j)))

            result.append(temp)

        return result
