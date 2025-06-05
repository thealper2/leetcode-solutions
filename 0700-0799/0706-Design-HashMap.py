class MyHashMap:
    def __init__(self):
        self.size = 2069 
        self.buckets = [[] for _ in range(self.size)]

    def _get_bucket(self, key: int) -> list:
        return self.buckets[key % self.size]

    def put(self, key: int, value: int) -> None:
        bucket = self._get_bucket(key)
        for i, (k, v) in enumerate(bucket):
            if k == key:
                bucket[i] = (key, value)
                return
        bucket.append((key, value))

    def get(self, key: int) -> int:
        bucket = self._get_bucket(key)
        for k, v in bucket:
            if k == key:
                return v
        return -1

    def remove(self, key: int) -> None:
        bucket = self._get_bucket(key)
        for i, (k, v) in enumerate(bucket):
            if k == key:
                del bucket[i]
                return