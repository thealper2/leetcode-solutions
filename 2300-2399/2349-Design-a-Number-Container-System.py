import heapq
from collections import defaultdict

class NumberContainers:

    def __init__(self):
        self.index_to_num = {}
        self.num_to_index = defaultdict(list)

    def change(self, index: int, number: int) -> None:
        self.index_to_num[index] = number
        heapq.heappush(self.num_to_index[number], index)

    def find(self, number: int) -> int:
        if number not in self.num_to_index:
            return -1

        heap = self.num_to_index[number]
        while heap and self.index_to_num[heap[0]] != number:
            heapq.heappop(heap)
        
        return heap[0] if heap else -1
