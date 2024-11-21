class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        first_row = "qwertyuiop"
        second_row = "asdfghjkl"
        third_row = "zxcvbnm"
        result = []
        for word in words:
            letters = set(word.lower())
            is_first_row = True
            is_second_row = True
            is_third_row = True
            
            for letter in letters:
                if letter not in first_row:
                    is_first_row = False
                
                if letter not in second_row:
                    is_second_row = False
                
                if letter not in third_row:
                    is_third_row = False
        
            if is_first_row or is_second_row or is_third_row:
                result.append(word)
            
        return result