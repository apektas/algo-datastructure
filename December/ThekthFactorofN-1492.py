class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        count = 0
        for i in range(1, n+1):
            if n % i == 0:
                count+=1
                if count == k: return i
        return -1

        # first version O(n) time -

        # second version we can divide n//2 + 1
    def kthFactorII(self, n: int, k: int) -> int:
        count = 0
        for i in range(1, n//2+1):
            if n % i == 0:
                count+=1
                if count == k: return i
        return  n if count+1==k  else -1

    # there is more faster version check it!!!