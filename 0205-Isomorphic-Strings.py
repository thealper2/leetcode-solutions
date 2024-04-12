def isIsomorphic(s: str, t: str) -> bool:
    return [s.index(x) for x in s] == [t.index(y) for y in t]
