class BrowserHistory:

    def __init__(self, homepage: str):
        self.history = []
        self.history.append(homepage)
        self.idx = 0

    def visit(self, url: str) -> None:
        del self.history[self.idx + 1:]
        self.history.append(url)
        self.idx += 1

    def back(self, steps: int) -> str:
        self.idx = max(0, self.idx - steps)
        return self.history[self.idx]

    def forward(self, steps: int) -> str:
        self.idx = min(len(self.history) - 1, self.idx + steps)
        return self.history[self.idx]