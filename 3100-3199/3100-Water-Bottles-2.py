class Solution:
    def maxBottlesDrunk(self, numBottles: int, numExchange: int) -> int:
        drunk = 0
        empty = 0
        current_exchange = numExchange
        full = numBottles

        while full > 0:
            drunk += full
            empty += full
            full = 0
            while empty >= current_exchange:
                empty -= current_exchange
                full += 1
                current_exchange += 1

        return drunk
