# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # time: O(N) - where N is the number of nodes in the BST. In the worst case we might be visiting all the nodes of the BST.
    # space: O(N) - This is because the maximum amount of space utilized by the recursion stack would be N since the height of a skewed BST could be N.
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root: return None
        # p and q smaller than root that means they are on the left side of the root
        if p.val < root.val and q.val < root.val:
            return self.lowestCommonAncestor(root.left, p, q)
        # p and q greater than root -  search on right
        if p.val > root.val and q.val > root.val:
            return self.lowestCommonAncestor(root.right, p ,q)
        # otherwise return root node
        return root

    # Time : O(N), where N is the number of nodes in the BST. In the worst case we might be visiting all the nodes of the BST.
    # Space : O(1).
    def lowestCommonAncestorIterative(self, root: TreeNode, p: TreeNode, q: TreeNode):
        while root:
            # on left side
            if p.val < root.val and q.val < root.val:
                root = root.left
            elif p.val > root.val and q.val > root.val:
                root = root.right
            else:
                return root
        return root

'''
       6
      / \
     2   8
    /\   /\
   0  4 7  9
      /\
     3  5
'''
root = TreeNode(6)
root.left = TreeNode(2)
root.left.left = TreeNode(0)
root.left.right = TreeNode(4)
root.left.right.left = TreeNode(3)
root.left.right.right = TreeNode(5)

root.right = TreeNode(8)
root.right.left = TreeNode(7)
root.right.right = TreeNode(9)

# 2, 4
print(Solution().lowestCommonAncestor(root, root.left, root.left.right).val)
print(Solution().lowestCommonAncestorIterative(root, root.left, root.left.right).val)

# 2, 8
print(Solution().lowestCommonAncestor(root, root.left, root.right).val)
print(Solution().lowestCommonAncestorIterative(root, root.left, root.right).val)