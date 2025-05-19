from typing import List


class Solution:
    def calculateTax(self, brackets: List[List[int]], income: int) -> float:
        tax = 0
        prev_upper = 0

        for upper, percent in brackets:
            if income >= upper:
                tax += (upper - prev_upper) * percent / 100
                prev_upper = upper

            else:
                tax += (income - prev_upper) * percent / 100
                return tax
            
        return tax