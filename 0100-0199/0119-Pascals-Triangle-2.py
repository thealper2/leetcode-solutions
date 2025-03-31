class Solution:
    def factorial(n):
        if n == 0:
            return 1
        else:
            return n * factorial(n - 1)

    def getRow(self, rowIndex: int) -> List[int]:
        result = []
        rowIndex += 1
        for i in range(rowIndex):
            temp = []
            for j in range(i + 1):
                if j == 0 or j == i:
                    temp.append(1)
                else:
                    temp.append(factorial(i) // (factorial(j) * factorial(i - j)))

            result.append(temp)

        return result[-1]
