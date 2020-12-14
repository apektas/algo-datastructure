from typing import List
# sayılar air craft içindeki people sayısını gösteriyor
# ard ard air craftlar inemiyor maximum person sayısını hesaplayan algorithma

'''
count of passengers and the game over here is to try to land as many passengers as possible while following
new rule that no two adjacent air crafts can land after each other.
'''
class Solution:
    def maxPassengerRecursive(self, passengers :List[int]) -> int:

        def maxPassenger(startIndex: int) -> int:
            if startIndex >=len(passengers): return 0

            chooseIndex = passengers[startIndex] + maxPassenger(startIndex + 2)
            notChooseIndex = maxPassenger(startIndex + 1)
            return max(chooseIndex, notChooseIndex)

        return maxPassenger(0)

    def maxPassengerTopDownWithMemoization(self, passengers :List[int]) -> int:

        cache = {}
        def maxPassenger(startIndex: int) -> int:
            if startIndex >=len(passengers): return 0
            if startIndex in cache: return cache[startIndex]

            chooseIndex = passengers[startIndex] + maxPassenger(startIndex + 2)
            notChooseIndex = maxPassenger(startIndex + 1)
            cache[startIndex] = max(chooseIndex, notChooseIndex)
            return cache[startIndex]
        return maxPassenger(0)

    def maxPassengerTopDownWithLRUCache(self, passengers :List[int]) -> int:
        from functools import lru_cache
        @lru_cache(None)
        def maxPassenger(startIndex: int) -> int:
            if startIndex >=len(passengers): return 0

            chooseIndex = passengers[startIndex] + maxPassenger(startIndex + 2)
            notChooseIndex = maxPassenger(startIndex + 1)
            return max(chooseIndex, notChooseIndex)
        return maxPassenger(0)

    '''
    dp[i] = max(dp[i+1], passengers[i] + dp[i+2]) 
    '''
    # O(n): space and O(n): time
    def maxPassengerWithBottomUp(self, passengers :List[int]) -> int:
        n = len(passengers)
        dp = [0]*(n+1)
        dp[n-1] = passengers[n-1]

        for i in range(n-2, -1, -1):
            chooseIndex = dp[i+2] + passengers[i]
            notChooseIndex = dp[i+1]
            dp[i] = max(chooseIndex, notChooseIndex)

        return dp[0]

    # O(1): space and O(n): time
    # this question is similar to climbing stairs
    def maxPassengerWithBottomUpSpaceOptimized(self, passengers :List[int]) -> int:
        n = len(passengers)
        nextNext, next = 0, passengers[n-1]

        for i in range(n-2, -1, -1):
            chooseIndex = nextNext + passengers[i]
            notChooseIndex = next
            current = max(chooseIndex, notChooseIndex)
            nextNext, next = next, current

        return next


# print(Solution().maxPassengerRecursive([155,55,2,96,67,203,3]))

# large values
# print(Solution().maxPassengerRecursive([155,11,5454,77,12,1,8,91,213,77878,9,12,14,1,66,55,2,96,67,203,3,155,11,5454,77,12,1,8,91,213,77878,9,12,14,1,66,55,2,96,67,203,3]))
print(Solution().maxPassengerTopDownWithMemoization([155,11,5454,77,12,1,8,91,213,77878,9,12,14,1,66,55,2,96,67,203,3,155,11,5454,77,12,1,8,91,213,77878,9,12,14,1,66,55,2,96,67,203,3]))
print(Solution().maxPassengerTopDownWithLRUCache([155,11,5454,77,12,1,8,91,213,77878,9,12,14,1,66,55,2,96,67,203,3,155,11,5454,77,12,1,8,91,213,77878,9,12,14,1,66,55,2,96,67,203,3]))
print(Solution().maxPassengerWithBottomUp([155,11,5454,77,12,1,8,91,213,77878,9,12,14,1,66,55,2,96,67,203,3,155,11,5454,77,12,1,8,91,213,77878,9,12,14,1,66,55,2,96,67,203,3]))
print(Solution().maxPassengerWithBottomUpSpaceOptimized([155,11,5454,77,12,1,8,91,213,77878,9,12,14,1,66,55,2,96,67,203,3,155,11,5454,77,12,1,8,91,213,77878,9,12,14,1,66,55,2,96,67,203,3]))



