class Solution:
    def hammingWeight(self, n: int) -> int:
        numberOf1Bits = 0
        count=0
        while n>0:
            if n & 1: numberOf1Bits+=1
            n = n>>1
            count+=1
        return (count, numberOf1Bits)
print(Solution().hammingWeight(23))

    # << left shift multiply by 2
    # >> right shift divide  by 2