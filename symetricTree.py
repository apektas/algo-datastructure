class TreeNode(object):
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right

class Solution(object):
    def isSymmetric(self, root):
        if(root is None): return True
        return self.isSymmetricHelper(root.left, root.right)

    def isSymmetricHelper(self, l1, l2):
        if(l1 == None and l2 == None): return True
        if(l1 == None and l2) or (l2 == None and l1): return False
        return l1.val == l2.val and self.isSymmetricHelper(l1.left, l2.right) and self.isSymmetricHelper(l1.right,l2.left)

# complexity :
# 3 + 2fn(n/2) ~ 2fn(n/2)
# for each iteration it will be 2fn(n/2)*2fn(n/2)... ..2fn(0) log(n) times if tree is balanced else it will be n times
# 2^log(n) = n
#

#         2
#     3       3
# 5    6    6   5
#         1
#     2      2
#   3   4   4  3


root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(2)
root.left.left = TreeNode(3)
root.left.right = TreeNode(4)

root.right.left = TreeNode(4)
root.right.right = TreeNode(3)

print(Solution().isSymmetric(root))