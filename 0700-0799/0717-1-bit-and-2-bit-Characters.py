from typing import List


class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        result = True
        for bit in bits[-2::-1]:
            if bit:
                result = not result
            else:
                break


        return result
