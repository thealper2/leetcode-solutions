def lemonadeChange(bills: List[int]) -> bool:
    bank = {5: 0, 10: 0, 20: 0}
    for bill in bills:
        print(bank)
        if bill == 5:
            bank[5] += 1

        elif bill == 10 and bank[5] > 0:
            bank[10] += 1
            bank[5] -= 1

        elif bill == 20 and ((bank[5] > 0 and bank[10] > 0) or bank[5] >= 3):
            if (bank[5] > 0 and bank[10] > 0):
                bank[5] -= 1
                bank[10] -= 1
            else:
                bank[5] -= 3

        else:
            return False

    return True
