#  1 <= N <= 10^9
from typing import List
class Solution:
    def prisonAfterNDays(self, cells: List[int], N: int) -> List[int]:
        cache = dict()
        for j in range(N):
            nextStep = [0]*len(cells)
            if str(cells) in cache: print("found in cache : {}".format(cache[str(cells)]))
            for i in range(1, len(cells)-1):
                prev, next = cells[i-1], cells[i+1]
                if (prev== 0 and next ==0) or (prev==1 and next==1):
                    nextStep[i]=1
                else:
                    nextStep[i]=0
            print(cells)
            cache[str(cells)]=j
            cells= nextStep
            #return result[0] cells[1:N-1] + result[0]

print(Solution().prisonAfterNDays([0,1,0,1,1,0,0,1], 20))