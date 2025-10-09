class Solution:
    def customSortString(self, order: str, s: str) -> str:
        rank = {c: i for i, c in enumerate(order)}
        return ''.join(sorted(s, key=lambda x: rank.get(x, len(order))))
