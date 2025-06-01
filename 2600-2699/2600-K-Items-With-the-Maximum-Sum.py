class Solution:
    def kItemsWithMaximumSum(self, numOnes: int, numZeros: int, numNegOnes: int, k: int) -> int:
        if k <= numOnes + numZeros:
            if numOnes < k:
                return numOnes
            else:
                return k
            
        else:
            neg = k - (numOnes + numZeros)
            return numOnes - neg