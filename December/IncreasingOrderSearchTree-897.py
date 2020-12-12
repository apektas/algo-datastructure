# Keep going to the left of the tree by appending the nodes to the stack and once you reach the
# leaf, then pop the stack and make the first popped node as root and then for rest of the nodes,
# append it to the right of the current root and make the left for each node as None

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from collections import deque
class Solution:

    def increasingBST(self, root: TreeNode) -> TreeNode:

        if not root: return None
        newRoot = None
        prev = None
        stack = deque()

        while stack or root:
            #  keep going left, until you hit a null
            while root:
                stack.append(root)
                root = root.left

            # pop from the stack and create the new root if not already created.
            root = stack.pop()
            if not newRoot: newRoot = root

            # assign the current  root element to previous element's right.
            if prev:
                prev.right = root
                root.left = None

            # point prev to current root and move current root to right.
            prev = root
            root = root.right

        return newRoot

