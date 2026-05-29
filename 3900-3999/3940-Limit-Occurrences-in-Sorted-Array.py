class Solution:
    def limitOccurrences(self, nums: list[int], k: int) -> list[int]:
        if not nums:
            return []
        
        result = []
        count = 1
        
        for i, num in enumerate(nums):
            if i == 0:
                result.append(num)
            elif num == nums[i - 1]:
                count += 1
                if count <= k:
                    result.append(num)
            else:
                count = 1
                result.append(num)
        
        return result