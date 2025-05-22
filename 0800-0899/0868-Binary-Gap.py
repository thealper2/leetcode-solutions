class Solution:
    def binaryGap(self, n: int) -> int:
        max_dist = 0
        last_one = None
        idx = 0

        while n > 0:
            if n % 2 == 1:
                if last_one is not None:
                    current_dist = idx - last_one
                    if current_dist > max_dist:
                        max_dist = current_dist
                    
                last_one = idx

            n //= 2
            idx += 1

        return max_dist