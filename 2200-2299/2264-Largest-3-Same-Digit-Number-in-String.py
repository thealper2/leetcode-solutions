class Solution:
    def largestGoodInteger(self, num: str) -> str:
        n = len(num)
        result = ""

        for i in range(0, n - 2):
            if len(set(num[i:i+3])) == 1:
                if num[i:i+3] > result:
                    result = num[i:i+3] 

        return result