from typing import List
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def rob(self, root: TreeNode) -> int:
        maxProfitWithRob = {}
        maxProfitWithoutRob = {}

        def maxProfitCanRobHouse(node):
            if not node: return 0
            if node in maxProfitWithRob: return maxProfitWithRob[node]
            maxProfitWithRobbing = node.val + maxProfitCannotRobHouse(node.left) + maxProfitCannotRobHouse(node.right)
            maxProfitWithoutRobbing = maxProfitCannotRobHouse(node)
            maxProfit = max(maxProfitWithRobbing,  maxProfitWithoutRobbing)
            maxProfitWithRob[node] = maxProfit
            return maxProfit

        def maxProfitCannotRobHouse(node):
            if not node: return 0
            if node in maxProfitWithoutRob: return maxProfitWithoutRob[node]
            maxProfit = 0 + maxProfitCanRobHouse(node.left) + maxProfitCanRobHouse(node.right)
            maxProfitWithoutRob[node] = maxProfit
            return maxProfit

        return  maxProfitCanRobHouse(root)

    def robI(self, nums: List[int]) -> int:
        maxProfit={}

        def robHelper(index, nums):
            if index > len(nums)-1: return 0
            if index in maxProfit: return maxProfit[index]
            maxProfitWithRob = nums[index] + robHelper(index+2, nums)
            maxProfitWithoutRob = 0 + robHelper(index+1, nums)
            maxProfit[index] = max(maxProfitWithRob, maxProfitWithoutRob)
            return maxProfit[index]

        return robHelper(0, nums)

    def robII(self, nums: List[int]) -> int:
        def rob(self, nums: List[int]) -> int:

            def robII(index, lastValInclude, nums):
                maxProfit = {}

                def robHelper(index, lastValInclude, nums):
                    if index > len(nums) - 1 - lastValInclude: return 0
                    if index in maxProfit: return maxProfit[index]
                    maxProfitWithRob = nums[index] + robHelper(index + 2, lastValInclude, nums)
                    maxProfitWithoutRob = 0 + robHelper(index + 1, lastValInclude, nums)
                    maxProfit[index] = max(maxProfitWithRob, maxProfitWithoutRob)
                    return maxProfit[index]

                return robHelper(index, lastValInclude, nums)

            if len(nums) == 1: return nums[0]
            return max(robII(0, 1, nums), robII(1, 0, nums))


print(Solution().robII( [1,2,3,1]))
print(Solution().robII( [2,3,2]))
print(Solution().robII( [1,2,4]))