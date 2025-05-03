class Solution:
    def reformatNumber(self, number: str) -> str:
        result = []
        count = 0

        for d in number:
            if d.isdigit():
                if count == 3:
                    count = 0
                    result.append("-")

                result.append(d)
                count += 1

        if count == 1:
            result[-2], result[-3] = result[-3], result[-2]

        return ''.join(result)