def isSubsequence(s: str, t: str):
    found, t_pointer = 0, 0
    while found < len(s) and t_pointer < len(t):
        if s[found] == t[t_pointer]:
            found += 1
        t_pointer += 1
    print(found, t_pointer)
    return found == len(s)
