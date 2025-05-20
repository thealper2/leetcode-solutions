class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False
        
        n = len(s)

        if s == goal:
            if n - len(set(s)) >= 1:
                return True
            else:
                return False
            
        diff = []
        for i in range(n):
            if s[i] != goal[i]:
                diff.append(i)
                if len(diff) > 2:
                    return False
                
        if len(diff) != 2:
            return False
        
        if s[diff[0]] == goal[diff[1]] and s[diff[1]] == goal[diff[0]]:
            return True
        
        return False