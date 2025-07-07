import re
from typing import List


class Solution:
    def validateCoupons(self, code: List[str], businessLine: List[str], isActive: List[bool]) -> List[str]:
        valid_coupons = []
        business_order = {"electronics": 0, "grocery": 1, "pharmacy": 2, "restaurant": 3}
        n = len(code)

        for i in range(n):
            if not code[i] or not re.fullmatch(r'^[a-zA-Z0-9_]+$', code[i]):
                continue

            if businessLine[i] not in business_order:
                continue

            if not isActive[i]:
                continue
            valid_coupons.append((business_order[businessLine[i]], businessLine[i], code[i]))
        
        valid_coupons.sort()
        result = [coupon[2] for coupon in valid_coupons]
        return result