class Spreadsheet:

    def __init__(self, rows: int):
        self.rows = rows
        self.grid = [[0] * 26 for _ in range(rows)]

    def setCell(self, cell: str, value: int) -> None:
        col = ord(cell[0]) - ord('A')
        row = int(cell[1:]) - 1
        self.grid[row][col] = value

    def resetCell(self, cell: str) -> None:
        col = ord(cell[0]) - ord('A')
        row = int(cell[1:]) - 1
        self.grid[row][col] = 0

    def getValue(self, formula: str) -> int:
        parts = formula[1:].split('+')
        total = 0
        for part in parts:
            if part[0].isalpha():
                col = ord(part[0]) - ord('A')
                row = int(part[1:]) - 1
                total += self.grid[row][col]

            else:
                total += int(part)

        return total
