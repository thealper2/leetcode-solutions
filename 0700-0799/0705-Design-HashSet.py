class MyHashSet:
    def __init__(self):
        self.n = 1000
        self.hashset = [[] for _ in range(self.n)]

    def add(self, key: int) -> None:
        if self.contains(key):
            return

        idx = key % 1000
        self.hashset[idx].append(key)

    def remove(self, key: int) -> None:
        if self.contains(key):
            idx = key % 1000
            self.hashset[idx].remove(key)

    def contains(self, key: int) -> bool:
        idx = key % 1000
        for k in self.hashset[idx]:
            if key == k:
                return True

        return False