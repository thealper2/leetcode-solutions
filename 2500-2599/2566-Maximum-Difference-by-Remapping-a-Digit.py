class Solution:
    def minMaxDifference(self, num: int) -> int:
        s = str(num)
        unique_digits = set(s)
        possible_numbers = []

        for digit in unique_digits:
            for new_digit in '0123456789':
                remapped_num = s.replace(digit, new_digit)
                possible_numbers.append(int(remapped_num))

        max_num = max(possible_numbers)
        min_num = min(possible_numbers)
        return max_num - min_num