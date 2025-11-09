from typing import List


class Solution:
    def minimumDistance(self, nums: List[int]) -> int:
        positions = {}
        for idx, num in enumerate(nums):
            if num not in positions:
                positions[num] = []

            positions[num].append(idx)

        min_distance = float('inf')
        for num, pos_list in positions.items():
            if len(pos_list) < 3:
                continue
            
            for j in range(1, len(pos_list) - 1):
                i = j - 1
                k = j + 1
                distance = abs(pos_list[i] - pos_list[j]) + abs(pos_list[j] - pos_list[k]) + abs(pos_list[k] - pos_list[i])
                min_distance = min(min_distance, distance)

        return min_distance if min_distance != float('inf') else -1
