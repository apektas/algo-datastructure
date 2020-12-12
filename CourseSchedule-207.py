from collections import defaultdict
class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        courses = defaultdict(list)
        for r in prerequisites:
            courses[r[0]].append(r[1])
        visited = [0]*numCourses
        for i in range(numCourses):
            if self.isCycle(courses, i, visited): return False
        return True


    def isCycle(self, courses, index, visited):
        if(visited[index] == 2): return True # if find processing node than it is a cycle
        visited[index] = 2 # set status processing
        for c in courses[index]:
            if(visited[c] !=1): # if not processed!
                if(self.isCycle(courses, c, visited)):
                    return True
        visited[index] = 1
        return False


print(Solution().canFinish(4,[[0,1], [2,0], [3,2]]))
