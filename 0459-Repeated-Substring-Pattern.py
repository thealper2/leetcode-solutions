def repeatedSubstringPattern(s: str) -> bool:
    res = ""
    for i in range(len(s) - 1):
        res += s[i]
        if s.count(res) * len(res) == len(s):
            return True

    return False
