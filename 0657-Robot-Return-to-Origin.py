def judgeCircle(moves: str) -> bool:
    # moves = [move for move in moves]
    if (moves.count("U") == moves.count("D")) & (moves.count("L") == moves.count("R")):
        return True
    else:
        return False
