'''
So, once again we have the following rules:

Elements in deque are always in decreasing order.
They are always elements from last sliding window of k elements.
It follows from here, that biggest element in current sliding window will be the 0-th element in it.
Complexity: time complexity is O(n), because we iterate over our elements and for each element it can be put inside and outside of our deque only once.
Space complexity is O(k), the maximum size of our deque.

'''

# https://leetcode.com/problems/sliding-window-maximum/discuss/951683/Python-Decreasing-deque-short-explained
from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        deq, n, ans = deque([0]), len(nums), []

        for i in range(n):
            # popped left because it is outside of the window's leftmost (i-k)
            while deq and deq[0] <= i-k:
                deq.popleft()

            # popped from deq because the last element < current element
            while deq and nums[i] >= nums[deq[-1]]:
                deq.pop()

            deq.append(i)
            # append the max element (i.e. deq[0] ) to the answer
            ans.append(nums[deq[0]])

        return ans[k-1:]