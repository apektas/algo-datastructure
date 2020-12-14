from typing import List
from functools import lru_cache
class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        nums = [1] + nums + [1]
        N = len(nums)
        # initialize dp with 0
        dp = [[0]*N  for i in range(N)]

        for i in range(N-2, 0, -1):
            for j in range(i, N-1):
                for k in range(i, j+1):
                    dp[i][j] = max(dp[i][j], nums[k]*nums[i-1]*nums[j+1] + dp[i][k-1] + dp[k+1][j])

        return dp[1][N-2]


    # TODO: fix this method
    def maxCoinsMemoizationLRU(self, nums: List[int]) -> int:
        # padding initial array
        nums = [1] + nums + [1]

        # cache this
        @lru_cache(None)
        def dp(left, right):

            # no more balloons can be added
            if left + 1 >= right: return 0

            # add each balloon on the interval and return the maximum score
            for lastToBurst in range(left+1, right):
                return max(nums[left] * nums[lastToBurst] * nums[right] + dp(left, lastToBurst) + dp(lastToBurst, right))

        # find the maximum number of coins obtained from adding all balloons from (0, len(nums) - 1)
        return dp(0, len(nums)-1)



print(Solution().maxCoins([3,1,5,8]))
print(Solution().maxCoinsMemoizationLRU([3,1,5,8]))


    # dp[i][j] = max points get from bursting from i to j does not matter how balloons burst

    # i-1, i ...... k ...... j, j+1
    # if k is the last to burst then we can get the following points
    # nums[k] * nums[i-1] * nums[j+1]

    # at that points then left side of the max points already stored in dp[i, k-1]
    # and the right max points stored in dp [k-1][j] you can refer the following list

    # i-1, [ i ......] k [...... j], j+1
    #       dp[i, k-1]   dp[k-1][j]    i<=k<=j




