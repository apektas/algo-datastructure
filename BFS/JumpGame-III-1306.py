from collections import deque
from typing import List
class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        queue, n = deque([start]), len(arr)
        visited = set()

        while queue:
            index = queue.popleft()
            if arr[index] == 0: return True

            for pos in (index-arr[index], index+arr[index]):
                if 0<= pos < n and pos not in visited:
                    visited.add(index)
                    queue.append(pos)

        return False

print(Solution().canReach([4,2,3,0,3,1,2], 0))
print(Solution().canReach([3,0,2,1,2],2))

'''
Complexity: Time complexity is O(n), where n is size of our arr: we only traverse indexes in this array. 
Space complexity is O(n) as well to keep array of visited nodes (or we can modify arr, but I think it is a bit of a cheat).
    # DFS version
    def canReach(self, arr, start):
        stack, visited, n = [start], set(), len(arr)
        
        while stack:
            pos = stack.pop()
            if arr[pos] == 0: return True
            visited.add(pos)
            cand1, cand2 = pos + arr[pos], pos - arr[pos]
            if cand1 <  n and cand1 not in visited: stack.append(cand1)
            if cand2 >= 0 and cand2 not in visited: stack.append(cand2)
                
        return False
'''