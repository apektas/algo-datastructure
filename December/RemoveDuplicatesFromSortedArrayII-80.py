from typing import List
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # nums >=2?
        slow, fast, N = 2, 2, len(nums)
        while fast < N:
            if nums[slow-2] != nums[fast]:
                nums[slow] = nums[fast]
                slow +=1
            fast+=1

        print(nums[:slow])
        return slow

'''
Let us use two pointers approach here: slow pointer and fast pointer, where slow will always be less or equal to fast. 
We are asked to remove duplicates only if we have more 2 of them, so we start with slow and fast equal to 2.
'''
print(Solution().removeDuplicates([0,0,1,1,1,1,2,3,3]))


