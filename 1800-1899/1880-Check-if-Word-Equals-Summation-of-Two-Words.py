class Solution:
    def isSumEqual(self, firstWord: str, secondWord: str, targetWord: str) -> bool:
        f, s, t = 0, 0, 0
        fl, sl, tl = len(firstWord), len(secondWord), len(targetWord)

        for i in range(fl):
            fl -= 1
            f += (int(ord(firstWord[i]) - ord('a'))) * (10 ** (fl))

        for i in range(sl):
            sl -= 1
            s += (int(ord(secondWord[i]) - ord('a'))) * (10 ** (sl))

        for i in range(tl):
            tl -= 1
            t += (int(ord(targetWord[i]) - ord('a'))) * (10 ** (tl))

        return (f + s) == t