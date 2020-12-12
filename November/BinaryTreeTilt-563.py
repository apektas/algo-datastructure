'''
Think about a recursive function. Beside the tilt of subtrees, we also need to get the sum of subtrees.
So I came up with the idea of sub function tilt(root), which returns the tuple (sum, tilt) of tree

'''
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.left = left
        self.right = right
        self.val = val

'''
Just traverse tree, using dfs, where we keep two values: sum of all tilts of current subtree and sum of nodes in current subtree. Then:

If we in None node, we return [0, 0]: we do nat have any subtree and tilt.
Let t1, s1 be tilt and sum of nodef for left subtree and t2, s2 for right subtree. Then how we can ealuate final sum of tilts for given node: it is abs(s1-s2) plus tilts for its children. To evaluate sum of all values in subtree we just need to evaluate s1+s2+node.val.
Complexity: time complexity is O(n), space complexity is O(h).
Complexity Analysis

Let NN be the number of nodes in the input tree.

Time Complexity: \mathcal{O}(N)O(N)

We traverse each node once and only once. During the traversal, we calculate the tilt value for each node.
Space Complexity: O(N)

Although the variables that we used in the algorithm are of constant-size, we applied recursion in the algorithm which incurs additional memory consumption in function call stack.

In the worst case where the tree is not well balanced, the recursion could pile up N times. As a result, the space complexity of the algorithm is O(N).

'''
class Solution:
    def findTilt(self, root:TreeNode ) -> int:
        # return result 0: sum 1: tilt
        def tilt(root: TreeNode) -> tuple[int, int]:
            if not root: return (0,0)
            left = tilt(root.left)
            right = tilt(root.right)
            return (left[0] + right[0] + root.val, left[1] + right[1] + abs(left[0]-right[0]))
        return tilt(root)[1]

root = TreeNode(val=21)
root.left = TreeNode(val=7,
             left=TreeNode(val=1, left=TreeNode(val=3), right=TreeNode(val=3)),
             right=TreeNode(val=1))
root.right= TreeNode(val=14, left=TreeNode(val=2), right=TreeNode(val=2))

print(Solution().findTilt(root))

# iterative solution
# https://leetcode.com/problems/binary-tree-tilt/discuss/102314/An-iterative-solution

'''
class Solution(object):
    def findTilt(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def tilt(root):
            if not root: return (0,0)
            left = tilt(root.left)
            right = tilt(root.right)
            return (left[0] + right[0] + root.val, abs(left[0]-right[0]) + left[1] + right[1])
        return tilt(root)[1]
        
'''

'''
queue += filter(None, (node.right, node.left))
is the same as: 
    if node.right:
        queue += [node.right]
    if node.left:
        queue += [node.left]


# random list
randomList = [1, 'a', 0, False, True, '0']

filteredList = filter(None, randomList)

print('The filtered elements are:')
for element in filteredList:
    print(element)

output: 
The filtered elements are:
1
a
True
0
'''