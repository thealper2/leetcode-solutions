class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        for _ in range(k):
            smallest = nums[0]
            idx = 0
            for i in range(1, len(nums)):
                if nums[i] < smallest:
                    smallest = nums[i]
                    idx = i

            nums[idx] *= multiplier

        return nums