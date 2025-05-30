from math import gcd
from collections import Counter
from typing import List

class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        count = Counter(deck).values()
        x = reduce(gcd, count)
        return x >= 2
