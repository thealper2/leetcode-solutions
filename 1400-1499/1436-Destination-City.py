from typing import List


class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        o = set()
        i = set()
        for path in paths:
            o.add(path[0])
            i.add(path[1])
        dest = i - o
        return dest.pop()