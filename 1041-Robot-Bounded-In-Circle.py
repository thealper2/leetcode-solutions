def isRobotBounded(instructions: str) -> bool:
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    x, y = 0, 0
    direction_index = 0

    for instruction in instructions:
        if instruction == 'G':
            dx, dy = directions[direction_index]
            x += dx
            y += dy
        elif instruction == 'L':
            direction_index = (direction_index - 1) % 4
        elif instruction == 'R':
            direction_index = (direction_index + 1) % 4

    return (x == 0 and y == 0) or direction_index != 0
