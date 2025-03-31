from typing import List


def merge(nums1: List[int], m: int, nums2: List[int], n: int) -> None:
    r1 = len(nums1) - m
    for i in range(r1):
        nums1.remove(nums1[-1])

    r2 = len(nums2) - n
    for i in range(r2):
        nums2.remove(nums2[-1])
    nums1.extend(nums2)
    nums1.sort()
    print(nums1)
