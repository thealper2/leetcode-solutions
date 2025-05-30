from typing import List


def strStr(haystack: str, needle: str) -> int:
    l = len(needle)
    for i in range(len(haystack) - l + 1):
        if haystack[i : i + l] == needle:
            return i
    return -1
