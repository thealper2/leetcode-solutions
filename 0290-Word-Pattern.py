def wordPattern(pattern: str, s: str) -> bool:
    m = {}
    words = s.split(" ")

    if len(words) != len(pattern):
        return False

    if len(set(pattern)) != len(set(words)):
        return False

    for i, word in enumerate(words):
        if word not in m:
            m[word] = pattern[i]
        elif m[word] != pattern[i]:
            return False

    print(m)
    return True
