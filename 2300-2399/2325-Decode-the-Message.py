class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        result = ""
        k_to_m = {" ": " "}
        current_char = 97

        for c in key:
            if c not in k_to_m:
                k_to_m[c] = chr(current_char)
                current_char += 1

        for c in message:
            result += k_to_m[c]

        return result