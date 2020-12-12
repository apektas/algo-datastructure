from collections import defaultdict
# https://www.youtube.com/watch?v=OsvbLAaRmu8
class Solution(object):
    def findMinHeightTrees(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        if n == 1: return [0]
        graph =  defaultdict(list)

        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        leaves = [ node for node in graph.keys() if len(graph[node])==1]

        while n > 2:
            n -= len(leaves)
            new_leaves = set()
            for leave in leaves:
                neighbor = graph[leave].pop()
                graph[neighbor].remove(leave)

                if len(graph[neighbor]) == 1:
                    new_leaves.add(neighbor)
            leaves = new_leaves

        return leaves

# https://leetcode.com/problems/minimum-height-trees/solution/
print(Solution().findMinHeightTrees(6, [[3,0],[3,1],[3,2],[3,4],[5,4]]))



