class Solution:
    def minimumIndex(self, capacity: list[int], itemSize: int) -> int:
        n = len(capacity)
        min_index = -1
        min_capacity = float('inf')
        
        for i in range(n):
            cap = capacity[i]
            if cap >= itemSize:
                if cap < min_capacity:
                    min_capacity = cap
                    min_index = i
        
        return min_index
