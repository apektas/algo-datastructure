from typing import List
class Solution:
    def searchWithDuplicate(self, nums, target):
        low, high = 0, len(nums)-1
        while low<=high:
            mid = (high + low) // 2
            if target == nums[mid]: return True

            ##  # Fail to estimate which side is sorted
            while low <mid and nums[low] == nums[mid]: low+=1
            while mid<high and nums[high] == nums[mid]: high-=1

            # check if left part is sorted
            if nums[low] <= nums[mid]:
                # target is out of the left
                if nums[low]<=target<nums[mid]:
                    high = mid - 1
                else:
                    # target lies within the left part
                    low = mid + 1

            else:
                # right part is sorted
                if nums[mid] < target <= nums[high]:
                    low = mid+1
                else:
                    # target lies within the right boundaries
                    high = mid -1

        return False

    def searchWithoutDuplicates(self, nums: List[int], target: int) -> int:
        low, high = 0, len(nums) - 1
        while low <= high:
            mid = low + (high - low) // 2
            if nums[mid] == target: return mid

            ## left part sorted
            if nums[low] <= nums[mid]:
                # target is on left
                if nums[low] <= target <= nums[mid]:
                    high = mid - 1
                else:
                    low = mid + 1


            # right part is sorted
            else:
                if nums[mid] <= target <= nums[high]:
                    low = mid + 1
                else:
                    high = mid - 1

        return -1

print(Solution().searchWithoutDuplicates([4,5,6,7,0,1,2], 0))
print(Solution().searchWithoutDuplicates([1,2], 2))
print(Solution().searchWithDuplicate([1,1,1,1,2,4], 4))