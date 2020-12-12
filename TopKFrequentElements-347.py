import heapq
from collections import defaultdict
class Solution:
    def topKFrequent(self, nums, k):
        occurrences = defaultdict(int)
        for num in nums:
            occurrences[num]+=1

        heap = []

        i = 0
        for num, count in occurrences.items():
            if i<k :
                heapq.heappush(heap, (count, num))
            else:
                if(heap[0][0] < count):
                    heapq.heappop(heap)
                    heapq.heappush(heap,(count, num))
            i+=1

        return [ h[1] for h in heap]

print(Solution().topKFrequent([1,1,2,2,2,3,4,4,4,4,4],2))