from typing import List

def lengthOfLastWord(s: str) -> int:
    s = " ".join(s.strip().split())
    last_word = s.split(" ")[-1]
    return len(last_word)
