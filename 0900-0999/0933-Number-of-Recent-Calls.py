class RecentCounter:

    def __init__(self):
        self.stack = []

    def ping(self, t: int) -> int:
        self.stack.append(t)
        while self.stack[0] < t - 3000:
            self.stack.pop(0)

        return len(self.stack)