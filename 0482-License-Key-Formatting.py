class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        s = s.upper().replace("-", "")
        result = []
        first_group = len(s) % k
        if first_group == 0:
            first_group = k

        result.append(s[:first_group])

        for i in range(first_group, len(s), k):
            result.append("-" + s[i : i + k])

        return "".join(result)