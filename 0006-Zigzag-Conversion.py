def convert(s: str, numRows: int) -> str:
    if numRows == 1 or numRows >= len(s):
        return s

    zigzag = [["" for _ in range(len(s))] for _ in range(numRows)]
    i, j = 0, 0
    down = True

    for idx in range(len(s)):
        zigzag[i][j] = s[idx]
        # print(i, j)

        if i == 0:
            down = True
        elif i == numRows - 1:
            down = False

        if down:
            i += 1
        else:
            i -= 1
            j += 1

    # print('\n'.join(['_'.join(['{:4}'.format(item) for item in row]) for row in zigzag]))
    concatenated_string = ""
    for row in zigzag:
        concatenated_string += "".join(row)

    return concatenated_string
