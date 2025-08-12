class Solution:
    def calculateScore(self, s: str) -> int:
        mirror = {}
        for i in range(26):
            mirror[chr(ord('a') + i)] = chr(ord('z') - i)
        
        n = len(s)
        marked = [False] * n
        unmarked_mirrors = {}
        total_score = 0
        
        for i in range(n):
            if marked[i]:
                continue
                
            current_char = s[i]
            mirror_char = mirror[current_char]
            if mirror_char in unmarked_mirrors:
                j = unmarked_mirrors[mirror_char].pop()
                if not unmarked_mirrors[mirror_char]:
                    del unmarked_mirrors[mirror_char]
                marked[i] = True
                marked[j] = True
                total_score += (i - j)
            else:
                if current_char not in unmarked_mirrors:
                    unmarked_mirrors[current_char] = []
                unmarked_mirrors[current_char].append(i)
        
        return total_score
