from typing import List

def plusOne(digits: List[int]) -> List[int]:
    text = ''.join([str(digit) for digit in digits])
    text = int(text) + 1
    return [int(digit) for digit in str(text)]
