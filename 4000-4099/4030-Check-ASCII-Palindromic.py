class Solution:
    def isPalindromic(self, s: str) -> bool:
        bin_s = ""
        for c in s:
            ord_c = ord(c)
            bin_ord_c = bin(ord_c)[2:].zfill(8)
            bin_s += bin_ord_c
        
        return bin_s == bin_s[::-1]