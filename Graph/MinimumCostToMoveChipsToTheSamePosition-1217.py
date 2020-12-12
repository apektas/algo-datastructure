class Solution(object):
    def minCostToMoveChips(self, position):
        """
        :type position: List[int]
        :rtype: int
        """
        even = odd = 0

        for p in position:
            if p % 2 == 0:
                odd += 1
            else:
                even += 1

        return min(odd, even)

print(Solution().minCostToMoveChips([1,2,2,3,4]))