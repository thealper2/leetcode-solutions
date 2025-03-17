def isPalindrome(s: str) -> bool:
    s = "".join(ch for ch in s if ch.isalnum()).lower()
    return s == s[::-1]
