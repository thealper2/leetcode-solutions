from typing import List


class Solution:
	def largestSumAfterKNegations(self, nums: List[int], k: int) -> int:
		n = len(nums)

		while k:
			min_ = float('inf')
			idx = 0
			for i in range(n):
				if nums[i] < min_:
					min_ = nums[i]
					idx = i

			nums[idx] = nums[idx] * -1
			k -= 1

		return sum(nums)
