import heapq
class Solution(object):


    # # O(k+(n-k)lgk) time, min-heap
    # def findKthLargest4(self, nums, k):
    #     heap = []
    #     for num in nums:
    #         heapq.heappush(heap, num)
    #     for _ in xrange(len(nums) - k):
    #         heapq.heappop(heap)
    #     return heapq.heappop(heap)
    ## number of ways to do!!!!
    # https://leetcode.com/problems/kth-largest-element-in-an-array/discuss/60306/Python-different-solutions-with-comments-(bubble-sort-selection-sort-heap-sort-and-quick-sort).
    # https://leetcode.com/problems/kth-largest-element-in-an-array/discuss/60547/Python-quick-select-(use-partition)-average-time-O(N)-and-worst-O(N2)
    def findKthLargest(self, nums, k):
        heap = nums[:k]
        heapq.heapify(heap)
        for n in nums[k:]:
            if(heap[0]<=n):
                heapq.heappushpop(heap, n)
        return heap[0]

print(Solution().findKthLargest([1,2,4,5,7],3))