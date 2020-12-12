#https://leetcode.com/problems/permutations/discuss/18239/A-general-approach-to-backtracking-questions-in-Java-(Subsets-Permutations-Combination-Sum-Palindrome-Partioning)

from typing import List
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        self.helperSubSet(nums, result,[], 0)
        return result


    def helperSubSet(self, nums, result, tmpList, startIndex):
        result.append(tmpList[:])
        for i in range(startIndex, len(nums)):
            tmpList.append(nums[i])
            self.helperSubSet(nums, result, tmpList, i+1)
            tmpList.pop()

    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        resultList = []
        self.helperWithDup(nums, resultList, [], 0)
        return resultList

    def helperWithDup(self, nums, resultList, tmpList, startIndex):
        resultList.append(tmpList[:])
        for i in range(startIndex, len(nums)):
            if i > startIndex and nums[i] == nums[i-1]: continue # skip duplicate
            tmpList.append(nums[i])
            self.helperWithDup(nums, resultList, tmpList, i+1)
            tmpList.pop()

    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ## not not increment the startIndex because we can use element again and again!
        result = []
        self.sumHelper(candidates, result, [], target, 0)
        return result

    def sumHelper(self, candidates, result, tmpList, target, startIndex):
        if target < 0: return
        if target == 0:
            result.append(tmpList[:])
        for i in range(startIndex, len(candidates)):
            tmpList.append(candidates[i])
            self.sumHelper(candidates, result, tmpList, target - candidates[i], i) ## try not add index and see
            tmpList.pop()

    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:

        result = []
        candidates.sort()
        self.helper(result, candidates, [], 0, target)
        return result

    def helper(self, result, candidates, tmpList, startIndex, target):
        if target == 0: result.append(tmpList[:])
        if target < 0: return

        for i in range(startIndex, len(candidates)):
            #if i > startIndex and candidates[i] == candidates[i - 1]: continue
            tmpList.append(candidates[i])
            self.helper(result, candidates, tmpList, i + 1, target - candidates[i])
            tmpList.pop()

# permutation https://leetcode.com/problems/permutations-ii/discuss/932924/Python-simple-dfsbacktracking-explained




    ##

    def partition(self, s: str) -> List[List[str]]:
        result = []
        self.partitionHelper(result, [], s, 0)
        return result

    def partitionHelper(self, result, tmpList, str, startIndex):
        if startIndex == len(str): result.append(tmpList[:])
        for i in range(startIndex, len(str)):
            if self.isPalindrome(str, startIndex, i):
                tmpList.append(str[startIndex:i+1])
                self.partitionHelper(result, tmpList, str, i+1)
                tmpList.pop()


    def isPalindrome(self, str, low, high):
        while low < high:
            if str[low] != str[high]: return False
            low+=1
            high-=1
        return True



nums = [1,2,3]
#nums = [1,2,2]
print(Solution().subsets(nums))
#print(Solution().subsetsWithDup(nums))
#print(Solution().partition("aab"))
# [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
