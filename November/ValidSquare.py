from typing import List
class Solution:
    def validSquare(self, p1: List[int], p2: List[int], p3: List[int], p4: List[int]) -> bool:
        points = [p1, p2, p3, p4]

        def distance(a:List[int], b:List[int])->int:
            return pow(a[0]-b[0], 2) + pow(a[1]-b[1],2)

        distances = []
        for index in range(len(points)):
            for subIndex in range(index +1 , len(points)):
                distances.append(distance(a=points[index], b=points[subIndex]))

        distances.sort()

        # 4 corner and 2 diagonal is equal
        ## edge case : [0,0], [0,0], [0,0] [0,0] -> distance[0] != 0
        return distances[0] != 0 and distances[0] == distances[1] and distances[0] == distances[2] and distances[0] == distances[3] and distances[4] == distances[5]

print(Solution().validSquare([0,0], [1,1], [1,0], [0,1]))
