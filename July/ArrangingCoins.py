class Solution:
    # write O(n) solution
    # also there is const time solution using math formula
    # https://www.youtube.com/watch?v=-cOyoXW73-I&list=PLJtzaiEpVo2wrUwkvexbC-vbUqVIy7qC-&index=31
    def arrangeCoins(self, n: int) -> int:
        # find the minimum k such that f(k)>=n

        low, high = 0, n
        while low<=high:
            mid = low + (high-low)//2 # // -> round down value
            sum=self._calculateSum(mid)
            if  sum ==n:
                return mid
            elif sum < n:
                low = mid + 1
            else:
                high = mid-1
        return high

    def _calculateSum(self, number):
        return number*(number+1)/2

print(Solution().arrangeCoins(5))
print(Solution().arrangeCoins(8))

