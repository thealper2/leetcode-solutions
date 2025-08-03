from typing import List


class Solution:
    def isTrionic(self, nums: List[int]) -> bool:
        n = len(nums)
        if n < 3:
            return False

        p_s = []
        for i in range(1, n - 1):
            if nums[i - 1] < nums[i] and nums[i] > nums[i + 1]:
                p_s.append(i)

        for p in p_s:
            for q in range(p + 1, n - 1):
                if nums[q] > nums[q + 1]:
                    continue

                increasing = True
                for k in range(q, n - 1):
                    if nums[k] >= nums[k + 1]:
                        increasing = False
                        break

                if increasing:
                    inc_p = True
                    for k in range(p):
                        if nums[k] >= nums[k + 1]:
                            inc_p = False
                            break

                    if not inc_p:
                        continue

                    dec_pq = True
                    for k in range(p, q):
                        if nums[k] <= nums[k + 1]:
                            dec_pq = False
                            break

                    if dec_pq:
                        return  True

        return False
