from collections import deque
from collections import defaultdict
def topologicalSort(vertices, edges):
    sortedOrder = []
    if vertices <=0: return sortedOrder

    # Initialize the graph
    # inDegree = defaultdict(int)
    # incoming edges on the node
    inDegree = { v: 0 for v in range(vertices)}
    graph = defaultdict(list)
    #graph = { v:[] for v in range(vertices)}

    for edge in edges:
        parent, child = edge
        graph[parent].append(child)
        inDegree[child]+=1

    # append 0 in degree to process
    sources = deque()
    for key in inDegree:
        if inDegree[key] == 0:
            sources.append(key)


    while sources:
        vertex = sources.popleft()
        sortedOrder.append(vertex)
        for child in graph[vertex]:
            inDegree[child] -=1
            if inDegree[child] == 0:
                sources.append(child)

    if len(sortedOrder) != vertices:
        return []

    return sortedOrder

print(str(topologicalSort(4, [[3,2], [3,0], [2,0], [2,1]])))

'''
In step ‘d’, each vertex will become a source only once and each edge will be accessed and removed once. 
Therefore, the time complexity of the above algorithm will be O(V+E), 
where ‘V’ is the total number of vertices and ‘E’ is the total number of edges in the graph.

Space Complexity #
The space complexity will be O(V+E), since we are storing all of the edges for each vertex in an adjacency list.


'''

# Problem 1: Find if a given Directed Graph has a cycle in it or not.