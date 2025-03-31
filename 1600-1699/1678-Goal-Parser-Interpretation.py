class Solution:
    def interpret(self, command: str) -> str:
        stack = []
        i = 0
        
        while i < len(command):
            if command[i] == 'G':
                stack.append('G')
                i += 1
            elif command[i:i+2] == '()':
                stack.append('o')
                i += 2
            elif command[i:i+2] == '(a':
                stack.append('al')
                i += 4
        
        return ''.join(stack)