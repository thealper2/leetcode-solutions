from typing import List


class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        n = len(boxes)
        answer = [0] * n
        ball_positions = [i for i in range(len(boxes)) if boxes[i] == '1']
        
        for i in range(n):
            total_operations = 0

            for pos in ball_positions:
                total_operations += abs(pos - i)
            answer[i] = total_operations
        
        return answer