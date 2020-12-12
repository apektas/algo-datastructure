# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def subtreeWithAllDeepest(self, root: TreeNode) -> TreeNode:
        def dfs(node):
            if not node: return 0, None
            leftDepth, leftNode = dfs(node.left)
            rightDepth, rightNode = dfs(node.rigt)
            if leftDepth > rightDepth:
                return leftDepth + 1, leftNode
            elif leftDepth < rightDepth:
                return rightDepth + 1, rightNode
            else:
                # does not matter return leftDepth+1 cause they have same depth
                return rightDepth + 1, node
        return dfs(root)[1]

# https://www.youtube.com/watch?v=IVS5POBWqTk
# This question is the same as 1123:
# https://leetcode.com/problems/lowest-common-ancestor-of-deepest-leaves/

# common ancestor

