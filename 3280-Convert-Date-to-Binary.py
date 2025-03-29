class Solution:
    def convertDateToBinary(self, date: str) -> str:
        result = []

        for num in date.split("-"):
            temp = []
            num = int(num)
            while num >= 1:
                temp.append(str(num % 2))
                num //= 2

            result.append("".join(temp[::-1]))

        return "-".join(result)