from typing import List
from collections import defaultdict
# https://leetcode.com/problems/permutations-ii/discuss/932924/Python-simple-dfsbacktracking-explained
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        counts = defaultdict(int)
        N = len(nums)
        for x in nums:
            counts[x] +=1

        ans = []
        def recurse(NLeft, currentArray):
            if NLeft == 0:
                # make a deep copy of the resulting permutation,
                # since the permutation would be backtracked later.
               ans.append(currentArray[:])
               return

            # 1 or 2
            # pick 1
                # then 1 or 2
                # pick 1
                    # then 2
            for x in counts.keys():
                if counts[x] > 0:
                    counts[x] -=1
                    recurse(NLeft - 1, currentArray + [x])
                    counts[x] +=1

        recurse(N, [])
        return ans

    def permute(self,  nums: List[int]) -> List[List[int]]:
        result = set()

        def permute(index, currentArray):
            if index == len(nums):
                result.add(tuple(currentArray[:]))
                return
            for i in range(len(nums)):
                currentArray[i] , currentArray[index] = currentArray[index], currentArray[i]
                permute(index+1, currentArray)
                currentArray[i] , currentArray[index] = currentArray[index], currentArray[i]

        permute(0, nums)

        return result









print(Solution().permuteUnique([1,1,1]))
print(Solution().permuteUnique([-1,2,-1,2,1,-1,2,1]))
