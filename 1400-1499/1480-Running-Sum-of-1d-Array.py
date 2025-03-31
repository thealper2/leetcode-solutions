class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        result = []
        count = 0

        for num in nums:
            count += num
            result.append(count)

        return result