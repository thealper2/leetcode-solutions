from typing import List


class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        result = []
        n = len(s)
        if n < 4 or n > 12:
            return result

        for i in range(1, min(4, n - 2)):
            for j in range(i + 1, min(i + 4, n - 1)):
                for k in range(j + 1, min(j + 4, n)):
                    part1 = s[:i]
                    part2 = s[i:j]
                    part3 = s[j:k]
                    part4 = s[k:]

                    if (len(part1) > 1 and part1[0] == '0') or (len(part2) > 1 and part2[0] == '0') or \
                    (len(part3) > 1 and part3[0] == '0') or (len(part4) > 1 and part4[0] == '0'):
                        continue
                    
                    if 0 <= int(part1) <= 255 and 0 <= int(part2) <= 255 and \
                    0 <= int(part3) <= 255 and 0 <= int(part4) <= 255:
                        result.append(f"{part1}.{part2}.{part3}.{part4}")

        return result
