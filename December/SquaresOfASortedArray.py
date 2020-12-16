from typing import List
class Solution:

    # O(nlog) solution
    # return sorted([i * i for i in nums])

    '''
        def sortedSquares(self, nums: List[int]) -> List[int]:
        ret = []
        for num in nums:
            ret.append(num ** 2)

        ret.sort()

        return ret

    '''

    def sortedSquares(self, nums: List[int]) -> List[int]:
        low, high = 0, len(nums)-1
        result = [0]*len(nums)
        leftIndex=high
        while low <= high:
            if pow(nums[low],2) > pow(nums[high],2):
                result[leftIndex] = pow(nums[low],2)
                low +=1
            else:
                result[leftIndex] = pow(nums[high],2)
                high -=1
            leftIndex -=1
        return result

    # no need extra variable for index
    '''
    def sortedSquares(self, A):
        answer = [0] * len(A)
        l, r = 0, len(A) - 1
        while l <= r:
            left, right = abs(A[l]), abs(A[r])
            if left > right:
                answer[r - l] = left * left
                l += 1
            else:
                answer[r - l] = right * right
                r -= 1
        return answer
    '''
print(Solution().sortedSquares([-7,-3,2,3,11]))
print(Solution().sortedSquares([-4,-1,0,3,10]))