import copy


class Solution(object):

    def _permuteHelper(self, nums, start=0):
        if start == len(nums)-1:
            return [copy.copy(nums)]  # or nums[:]
        result = []
        for i in range(start, len(nums)):
            nums[i], nums[start] = nums[start], nums[i]
            result += self._permuteHelper(nums, start+1)
            nums[i], nums[start] = nums[start], nums[i]
        return result

    def permute(self, nums):
        return self._permuteHelper(nums)

# driver function
permutataions = Solution().permute([2,4,6,8])

for i in range(0,len(permutataions),6):
    print(permutataions[i:i+6])



