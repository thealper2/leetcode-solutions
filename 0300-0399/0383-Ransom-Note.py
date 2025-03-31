def canConstruct(ransomNote: str, magazine: str) -> bool:
    for char in ransomNote:
        if magazine.count(char) < ransomNote.count(char):
            return False

    return True
