class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False

        reversed_x = 0
        temp = x
        while temp > 0:
            r = temp % 10
            reversed_x = reversed_x * 10 + r
            temp = temp // 10

        if x == reversed_x:
            return True
        else:
            return False
