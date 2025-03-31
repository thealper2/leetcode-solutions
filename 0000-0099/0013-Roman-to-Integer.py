from typing import List


def romanToInt(s: str) -> int:
    roman_values = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}

    result = 0
    prev_value = 0

    for c in s:
        value = roman_values[c]
        result += value
        if value > prev_value:
            result -= 2 * prev_value
        prev_value = value

    return result
