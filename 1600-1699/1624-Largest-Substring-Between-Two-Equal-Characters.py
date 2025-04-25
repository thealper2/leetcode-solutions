class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        char_indices = {}
        max_length = -1

        for index, char in enumerate(s):
            if char in char_indices:
                first_occurence = char_indices[char]
                current_length = index - first_occurence - 1
                if current_length > max_length:
                    max_length = current_length

            else:
                char_indices[char] = index

        return max_length