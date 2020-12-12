from typing import List
class Solution:
    def flipAndInvertImage(self, A: List[List[int]]) -> List[List[int]]:
        return [[1 - i for i in row[::-1]] for row in A]
        # return [[ 1^i for i in row[::-1]] for row in A]

A = [[1,1,0],[1,0,1],[0,0,0]]
print(Solution().flipAndInvertImage(A))
A = [[1,1,0,0],[1,0,0,1],[0,1,1,1],[1,0,1,0]]
print(Solution().flipAndInvertImage(A))

