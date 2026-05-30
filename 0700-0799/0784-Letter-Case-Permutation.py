class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        result = ['']
        for c in s:
            if c.isalpha():
                new_result = []
                for r in result:
                    new_result.append(r + c.lower())
                    new_result.append(r + c.upper())

                result = new_result
            else:
                result = [r + c for r in result]

        return result