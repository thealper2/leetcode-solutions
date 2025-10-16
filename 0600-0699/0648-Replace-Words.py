from typing import List


class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        roots = set(dictionary)
        words = sentence.split()

        result = []
        for word in words:
            replacement = word
            for i in range(1, len(word) + 1):
                prefix = word[:i]
                if prefix in roots:
                    replacement = prefix
                    break

            result.append(replacement)
        
        return ' '.join(result)
