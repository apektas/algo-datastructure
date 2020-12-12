class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root == None: return 0
        return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1




#[3, [9,20] [15,7]]
  #   3
  #  / \
  # 9  20
  #   /  \
  #  15   7

root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)

root.right.left = TreeNode(15)
root.right.right = TreeNode(7)

print(Solution().maxDepth(root))