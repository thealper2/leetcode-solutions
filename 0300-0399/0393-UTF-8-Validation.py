from typing import List


class Solution:
    def validUtf8(self, data: List[int]) -> bool:
        binary_data = [bin(item)[2:].rjust(8, '0') for item in data]
        byte = 0

        for b in binary_data:
            if byte == 0:
                for bit in b:
                    if bit == '1':
                        byte += 1
                    else:
                        break

                if byte == 0:
                    continue
                if byte == 1 or byte > 4:
                    return False
                byte -= 1
            else:
                if not b.startswith('10'):
                    return False
                byte -= 1

        return byte == 0
