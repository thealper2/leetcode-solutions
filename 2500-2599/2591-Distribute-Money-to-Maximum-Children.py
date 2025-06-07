class Solution:
    def distMoney(self, money: int, children: int) -> int:
        if money < children:
            return -1
        
        if money == children:
            return 0
        
        result = 0
        for i in range(1, children + 1):
            if money - 8 >= children - i:
                money -= 8
                result += 1
            else:
                if children - i == 0 and money == 4:
                    result -= 1

                money = 0
                break

        if money > 0:
            result -= 1

        return result