class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [0] * (n+1)
        dp[1] = 1
        if n <= 1: return dp[n]
        dp[2] = 2

        for i in range(3, n+1):
            dp[i] =  dp[i-1] + dp[i-2]

        return dp[n]

    # similar to fibonacci -  no need to O(n) space
    # previous - previousPrev and current are enough
    def climbStairsII(self, n: int) -> int:
        pass

    # top-down approach
    def climbStairsRecursive(self, n):
        if n <= 1: return 1
        return self.climbStairsRecursive(n-1) + self.climbStairsRecursive(n-2)

    def climbStairsTopDownMemoization(self, n):
        cache = {}

        def climbStairsRec(n):
            if n <=1: return 1
            if n in cache: return cache[n]
            cache[n] = climbStairsRec(n-1) + climbStairsRec(n-2)
            return cache[n]

        return climbStairsRec(n)
print(Solution().climbStairs(2))
print(Solution().climbStairsTopDownMemoization(20))