class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left=left
        self.right=right
class Solution:
    # return (isBalanced, height)
    def isBalanced(self, root):

        def isBalanceHelper(root):
            if not root: return (True, 0)
            lBalanced, lHeight = isBalanceHelper(root.left)
            rBalanced, rHeight = isBalanceHelper(root.right)
            return (lBalanced and rBalanced and abs(rHeight-lHeight)<=1, max(lHight, rHeight)+1)

        return isBalanceHelper(root)[0]

    # Based on post-order traversal
    def isBalancedIterative(self, root):
        stack, node, last, depths = [], root, None, {}
        while stack or node:
            if node:
                stack.append(node)
                node = node.left
            else:
                node = stack[-1]
                if not node.right or last == node.right:
                    node = stack.pop()
                    left, right  = depths.get(node.left, 0), depths.get(node.right, 0)
                    if abs(left - right) > 1: return False
                    depths[node] = 1 + max(left, right)
                    last = node
                    node = None
                else:
                    node = node.right
        return True