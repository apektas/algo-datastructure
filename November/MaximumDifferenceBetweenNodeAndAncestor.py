class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxAncestorDiff(self, root:TreeNode ) -> int:
        if not root: return 0
        return self.helper(root, root.val, root.val)

    def helper(self, root:TreeNode, low :int , high: int) -> int:
        if not root: return high-low

        low  = min(root.val, low)
        high = max(root.val, high)

        return max(self.helper(root.left, low, high ), self.helper(root.right, low, high))

root = TreeNode(val=1, right=TreeNode(val=2, right=TreeNode(val=0, left=TreeNode(val=4))))
print(Solution().maxAncestorDiff(root))


# iterative solution : https://leetcode.com/problems/maximum-difference-between-node-and-ancestor/discuss/274614/Python-28ms-13.7MB-nonrecur