
# S1 + S2 = SUM_N
# if SUM_N % 2 == 0 then there might be a solution
# else: no possible solution

class Solution:
    def canPartition(self, nums ):
        N = len(nums)
        total = sum(nums)
        if total % 2 : return False
        totalHalf = total // 2
        cache = {}



        # index -> 1 to N : 1-200
        # totalLeft: 1 to 100
        # totalPossible inputs = 20000 = O(N^2*C)

        # can we reach exactly the sum of totalLeft
        def canP(index, totalLeft):
            if totalLeft == 0: return True
            if totalLeft < 0: return False
            if index == N: return False

            if (index, totalLeft) in cache:
                return cache[(index, totalLeft)]

            # do we use this number or not
            possibleIfUsed = canP(index+1, totalLeft - nums[index])
            possibleIfNotUsed = canP(index+1, totalLeft )

            cache[(index, totalLeft)] = possibleIfUsed or possibleIfNotUsed
            return cache[(index, totalLeft)]

        return canP(0, totalHalf)