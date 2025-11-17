class Solution:
    def minLengthAfterRemovals(self, s: str) -> int:
        stack = []
        for c in s:
            if stack and ((stack[-1] == 'a' and c == 'b') or (stack[-1] == 'b' and c == 'a')):
                stack.pop()
            else:
                stack.append(c)
        return len(stack)
