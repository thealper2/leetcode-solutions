class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        d = {}
        for jewel in jewels:
            for stone in stones:
                if jewel == stone:
                    if jewel not in d:
                        d[jewel] = 1
                    else:
                        d[jewel] += 1

        return sum([v for v in d.values()])