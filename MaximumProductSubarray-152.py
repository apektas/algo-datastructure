class Solution(object):
    def maxProduct(self, nums):
        maxSoFar = nums[0]
        minSoFar = nums [0]
        maxCur = nums[0]
        for i in range(1, len(nums)):
            tmp = maxSoFar
            maxCur = max(maxCur * nums[i], nums[i])
            maxSoFar = max(max(tmp * nums[i] , minSoFar * nums[i]), maxCur)
            minSoFar = min(min(minSoFar * nums[i], tmp * nums[i]), minSoFar)
        return maxSoFar
print(Solution().maxProduct([2,3,-2,4]))
print(Solution().maxProduct([-2,0,-1]))