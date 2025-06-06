from typing import List


class OrderedStream:
    def __init__(self, n: int):
        self.n = n
        self.stream = [None] * n
        self.ptr = 0

    def insert(self, idKey: int, value: str) -> List[str]:
        self.stream[idKey - 1] = value

        if idKey - 1 > self.ptr:
            return []

        while self.ptr < self.n and self.stream[self.ptr]:
            self.ptr += 1

        return self.stream[idKey-1:self.ptr]