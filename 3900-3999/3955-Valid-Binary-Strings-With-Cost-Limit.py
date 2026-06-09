class Solution:
    def generateValidStrings(self, n: int, k: int) -> list[str]:
        result = []
        for num in range(2 ** n):
            binary_num = bin(num)[2:].zfill(n)
            if '11' in binary_num:
                continue

            cost = sum([i for i, char in enumerate(binary_num) if char == '1'])
            if cost <= k:
                result.append(binary_num)

        return result
