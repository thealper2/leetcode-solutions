class Solution:
    def checkRecord(self, s: str) -> bool:
        n = len(s)
        a_seen = False

        for i in range(n):
            if s[i:i+3] == 'LLL':
                return False

            if s[i] == 'A':
                if a_seen:
                    return False

                a_seen = True

        return True