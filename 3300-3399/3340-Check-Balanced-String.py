class Solution:
    def isBalanced(self, num: str) -> bool:
        result = 0
        for i in range(len(num)):
            if i % 2 == 0:
                result += int(num[i])
            else:
                result -= int(num[i])

        return result == 0