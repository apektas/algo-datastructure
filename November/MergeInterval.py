from typing import List
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda a:a[0])
        start, end = intervals[0]
        result = []
        for i in range(1, len(intervals)):
            nextInterval = intervals[i]
            if nextInterval[0]<=end:
                end = max(nextInterval[1], end)
            else:
                result.append([start, end])
                start, end = nextInterval
        result.append([start, end])
        return result


print(Solution().merge([[1,3],[2,6],[8,10],[15,18]]))
print(Solution().merge([[1,4],[2,3]]))