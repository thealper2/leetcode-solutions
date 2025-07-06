class Solution:
    def concatHex36(self, n: int) -> str:
        alphabet = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        base36 = ''
        n_squared = n ** 2
        n_cubed = n ** 3
        hex_part = hex(n_squared)[2:].upper()
        
        if n_cubed == 0:
            return alphabet[0]
        
        while n_cubed != 0:
            n_cubed, i = divmod(n_cubed, 36)
            base36 = alphabet[i] + base36
        
        return hex_part + base36