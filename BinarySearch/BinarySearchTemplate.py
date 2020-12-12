from typing import List
class Solution:
    def firstBadVersion(self, n) -> int:
        left, right = 1, n
        while left < right:
            mid = left + (right - left) // 2
            if isBadVersion(mid): ## provided by leetcode
                right = mid
            else:
                left = mid + 1
        return left
# There’s one thing I’d like to point out. Remember I say that we usually look for the minimal k value satisfying certain condition?
# But in this problem we are searching for maximal k value instead. Feeling confused? Don’t be. Actually, the maximal k satisfying isBadVersion(k) is False is just equal to the minimal k satisfying isBadVersion(k) is True minus one. This is why I mentioned earlier that we need to decide which value to return, left or left — 1 .
    def mySqrt(self, x: int) -> int:
        left, right = 0, x+1
        while left<right: ## sometimes <= sometimes < ?
            mid = left + (right-left)//2
            if mid **2 <= x:
                left = mid+1
            else:
                right=mid

        return left-1

# Very classic application of binary search. We are looking for the minimal k satisfying nums[k] ≥ target, and we can just copy-paste our template. Notice that our solution is correct regardless of whether the input array nums has duplicates. Also notice that the input target might be larger than all elements in nums and thus needs to placed at the end of the array. That’s why we should initialize right = len(nums) instead of right = len(nums) — 1 .
    def searchInsertPosition(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums)
        while left < right:
            mid = left + (right-left)//2
            if nums[mid]>=target:
                right = mid
            else: left = mid+1
        return left


    def shipWithinDays(self, weights: List[int], D: int) -> int:
        def isFeasible(capacity) -> bool:
            days = 1; total =0
            for weight in weights:
                total +=weight
                if total > capacity:
                    total = weight
                    days+=1
                    if days>D: return False
            return True

        left, right = max(weights), sum(weights)
        while left < right:
            mid = left + (right-left)//2
            if isFeasible(mid):
                right =mid
            else: left = mid+1

        return left



