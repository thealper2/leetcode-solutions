from typing import List


class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        n = len(nums)

        for i in range(n):
            for j in range(0, n - i - 1):
                if nums[j + 1] < nums[j]:
                    nums[j], nums[j + 1] = nums[j + 1], nums[j]

        prefix = [0]
        for num in nums:
            prefix.append(prefix[-1] + num)
        
        answer = []
        for q in queries:
            left, right = 0, len(prefix) - 1
            best_k = 0
            while left <= right:
                mid = (left + right) // 2
                if prefix[mid] <= q:
                    best_k = mid
                    left = mid + 1
                else:
                    right = mid - 1
            answer.append(best_k)
            
        return answer