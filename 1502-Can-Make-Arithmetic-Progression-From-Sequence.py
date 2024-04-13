from typing import List

def canMakeArithmeticProgression(arr: List[int]) -> bool:
    arr = sorted(arr)
    cur = arr[1] - arr[0]
    for i in range(len(arr)-1):
        dif = arr[i+1] - arr[i]
        if cur != dif:
            return False
    return True
