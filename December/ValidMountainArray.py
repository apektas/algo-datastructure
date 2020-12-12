from typing import List
class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        # there should be one pick!
        if len(arr)<3: return False
        index = 0;
        N = len(arr)

        while index < N -1:
            if (arr[index] > arr[index+1]):
                break
            elif arr[index] == arr[index+1]: return False
            index += 1
        if index == 0: return False
        #print("pick value is {}".format(arr[index]))
        if index == N-1: return False
        while index < N-1:
            if arr[index] <= arr[index+1]:
                return False
            index +=1

        return True

    # this comes from leetcode
    def validMountainArrayVal(self, arr: List[int]) -> bool:
        if len(arr) < 3 or arr[0] >= arr[1]: # take edge cases carefully
            return False

        uphill = True

        for i in range(1, len(arr)):
            if uphill:
                if arr[i - 1] >= arr[i]:
                    uphill = False
            if not uphill:
                if arr[i - 1] <= arr[i]:
                    return False
        return not uphill


    '''
    Let us start from the left of our arr and go to the right until it is possible, that is until our data is increasing. 
    Also we start from the end and go to the left until our data is decreasing. 
    If we met somewhere in the middle in point, which is neither 0 nor n-1, 
    it means that we found our mountain, in other case array is not mountain.
    Complexity: we pass over our data only once, so time complexity is O(n); space complexity is O(1).

    class Solution:
        def validMountainArray(self, arr):
            n = len(arr)
            beg, end = 0, n - 1
            while beg != n-1 and arr[beg + 1] > arr[beg]: beg += 1
            while end != 0 and arr[end - 1] > arr[end]: end -= 1 
            return beg == end and end != n-1 and beg != 0
    
845. Longest Mountain in Array: 
https://leetcode.com/problems/longest-mountain-in-array/discuss/937652/Python-one-pass-O(1)-space-explained
1671 Minimum Number of Removals to Make Mountain Array: 
https://leetcode.com/problems/minimum-number-of-removals-to-make-mountain-array/discuss/952053/Python-3-solutions%3A-LIS-dp-O(n-log-n)-explained
'''
# https://leetcode.com/problems/valid-mountain-array/discuss/966752/python-one-pass-explained
print(Solution().validMountainArray([1,2,3]))
print(Solution().validMountainArray([1,3,2]))
print(Solution().validMountainArray([0,3,2,1]))
print(Solution().validMountainArray([0,1,2,4,2,1]))
print(Solution().validMountainArray([9,8,7,6,5,4,3,2,1,0]))
print(Solution().validMountainArray([0,1,2,3,4,5,6,7,8,9]))