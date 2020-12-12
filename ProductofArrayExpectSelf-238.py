class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        n = len(nums)
        result = [1] * n

        for i in range(1, len(nums)):
            result[i] = result[i - 1] * nums[i - 1]

        multiply = 1
        for i in range(n - 1, -1, -1):
            result[i] = result[i] * multiply
            multiply *= nums[i]

        return result


print(Solution().productExceptSelf([1,2,3,4]))