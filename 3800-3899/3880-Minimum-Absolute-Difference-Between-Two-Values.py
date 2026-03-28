class Solution:
    def minAbsoluteDifference(self, nums: list[int]) -> int:
        n = len(nums)
        min_dif = float('inf')
        
        last_one = -1
        last_two = -1
        
        for i, num in enumerate(nums):
            if num == 1:
                if last_two != -1:
                    min_dif = min(min_dif, i - last_two)

                last_one = i
            
            elif num == 2:
                if last_one != -1:
                    min_dif = min(min_dif, i - last_one)
                
                last_two = i
        
        return min_dif if min_dif != float('inf') else -1
