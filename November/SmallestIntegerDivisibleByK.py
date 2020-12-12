class Solution:
    def smallestRepunitDivByK(self, K: int) -> int:
        remaining = 0
        length = 0
        for i in range(K+1):
            remaining = 10 * remaining +1
            remaining = remaining % K
            length+=1
            if not remaining: return length
        return -1

print(Solution().smallestRepunitDivByK(3))
print(Solution().smallestRepunitDivByK(2))