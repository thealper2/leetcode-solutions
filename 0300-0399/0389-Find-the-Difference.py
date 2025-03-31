def findTheDifference(s: str, t: str) -> str:
    if len(s) == 0:
        return t

    for letter in t:
        if s.count(letter) != t.count(letter):
            return letter
