class Solution:
    def countBalls(self, lowLimit: int, highLimit: int) -> int:
        boxes = [[] for _ in range(45)]
        max_len = 1

        for i in range(lowLimit, highLimit + 1):
            s = 0
            num = i
            while num > 0:
                s += num % 10
                num //= 10

            boxes[s - 1].append(i)

            if len(boxes[s - 1]) > max_len:
                max_len = len(boxes[s - 1])

        return max_len

