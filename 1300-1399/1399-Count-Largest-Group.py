class Solution:
    def countLargestGroup(self, n: int) -> int:
        if n < 10:
            return n
        
        groups = [[] for _ in range(36)]
        
        max_len = 1
        
        for i in range(1, n + 1):
            s = 0
            num = i
            while num > 0:
                s += num % 10
                num //= 10
            
            groups[s - 1].append(i)
            
            if len(groups[s - 1]) > max_len:
                max_len = len(groups[s - 1])
        
        return sum(1 for group in groups if len(group) == max_len)
