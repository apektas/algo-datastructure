from collections import defaultdict, OrderedDict, deque
import string
class Solution:
    def alienOrder(self, words):
        if not words: return

        # build adjacency list and inDegree list
        graph = defaultdict(set)
        # count if something comes first or not
        # if in degree = 0  then it is the beginning of the alphabet
        inDegree = {ch: 0 for ch in list(string.ascii_lowercase)}
        # inDegree = [ 0 for _ in range(26) ]
        # if we do not know the ordering then ascii ordering preserved!

        for i in range(len(words)-1):
            firstWord = words[i]
            secondWord =  words[i+1]

            # zip !!!
            # Make an iterator that aggregates elements from each of the iterables.
            #
            # Returns an iterator of tuples, where the i-th tuple contains the i-th element from each of the argument sequences or iterables.
            # The iterator stops when the shortest input iterable is exhausted.
            # With a single iterable argument, it returns an iterator of 1-tuples. With no arguments, it returns an empty iterator.
            # Equivalent to:  # zip('ABCD', 'xy') --> Ax By

            for outChar, inChar in zip(firstWord, secondWord):
                if outChar!=inChar:
                    # do some cool logic
                    if outChar not in graph[inChar]:
                        graph[inChar].add(outChar)
                        inDegree[outChar]+=1
                    ## why we need break ? because the first different word is matter others not!
                    break
            else: # if we did not hit break
                if len(secondWord) < len(firstWord): return ""
        queue = deque()
        for k, v in inDegree.items():
            if k in graph and v==0:
                queue.append(k)

        result = []

        ## bread first search
        while queue:
            node = queue.popleft()
            result.append(node)

            for neighbor in graph[node]:
                inDegree[neighbor]-=1
                if inDegree[neighbor] == 0:
                    queue.append(neighbor)

        if len(result) != len(graph): return ''
        return ''.join(result)
# order relationship : we can use the graph to represent the relationship
# Topological sort can be handy.
# Directed acyclic graph

# 1- build graph
# 2- topological sorting

print(Solution().alienOrder(["wrt", "wrf", "er", "ett", "rftt"]))
