from typing import List

def longestCommonPrefix(strs: List[str]) -> str:
    shortest_word = min(strs, key=len)
    ans = ""
    for i, char in enumerate(shortest_word):
        for word in strs:
            if word[i] != char:
                return shortest_word[:i]
        ans += char
    return ans
