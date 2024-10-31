class Solution:
    def isValid(self, s: str) -> bool:
        bracket_stack = []
        open_brackets = ["(", "{", "["]
        close_brackets = [")", "}", "]"]

        for c in s:
            if c in open_brackets:
                bracket_stack.append(c)
            
            elif c in close_brackets:
                if not bracket_stack:
                    return False

                top = bracket_stack.pop()
                if (top == '(' and c != ')') or (top == '{' and c != '}') or (top == '[' and c != ']'):
                    return False

        return len(bracket_stack) == 0 
