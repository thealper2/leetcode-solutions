from typing import List


def tictactoe(moves: List[List[int]]) -> str:
    board = [[" " for _ in range(3)] for _ in range(3)]
    player = "X"
    winner = ""
    for move in moves:
        board[move[0]][move[1]] = player
        if player == "X":
            player = "O"
        else:
            player = "X"

    for row in board:
        if row[0] == row[1] == row[2] and row[0] != " ":
            winner = row[0]

    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != " ":
            winner = board[0][col]

    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != " ":
        winner = board[0][0]
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != " ":
        winner = board[0][2]

    # print(''.join([elem for row in board for elem in row]))
    if winner == "X":
        return "A"
    elif winner == "O":
        return "B"
    elif " " in "".join([elem for row in board for elem in row]):
        return "Pending"
    else:
        return "Draw"
