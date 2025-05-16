class Solution:
    def numDifferentIntegers(self, word: str) -> int:
        unique_numbers = set()
        current_num = []
        
        for c in word:
            if c.isdigit():
                current_num.append(c)
            else:
                if current_num:
                    num_str = ''.join(current_num).lstrip('0')
                    num_str = num_str if num_str else '0'
                    unique_numbers.add(num_str)
                    current_num = []

        if current_num:
            num_str = ''.join(current_num).lstrip('0')
            num_str = num_str if num_str else '0'
            unique_numbers.add(num_str)
        
        return len(unique_numbers)