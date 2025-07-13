class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        dirs = path.split('/')

        for dir_ in dirs:
            if dir_ == '.' or dir_ == '':
                continue
            elif dir_ == '..':
                if stack:
                    stack.pop()
            else:
                stack.append(dir_)

        path = '/' + '/'.join(stack)
        return path
