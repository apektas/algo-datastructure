# https://leetcode.com/problems/validate-binary-search-tree/discuss/32112/Learn-one-iterative-inorder-traversal-apply-it-to-multiple-tree-questions-(Java-Solution)
# k-th smallest element - nice question
# binary tree in order traversal

# https://leetcode.com/problems/two-sum-iv-input-is-a-bst/discuss/106067/C%2B%2BPython-Straight-Forward-Solution
# https://leetcode.com/problems/two-sum-iv-input-is-a-bst/discuss/106059/JavaC%2B%2B-Three-simple-methods-choose-one-you-like


from collections import deque
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
class Solution:

    def validateBST(self, root):

        def validateHelper(root, lessThan, largerThan):
            if not root: return True
            if root.val <= lessThan or root.val >= largerThan: return False
            return validateHelper(root.left, min(root.val, lessThan), root.val) and validateHelper(root.right, lessThan, max( largerThan, root.val) )

        return validateHelper(root, float('-inf'), float('+inf'))

    ''' if BST then in-order traversal -> prev < element'''
    ## key point need to use other binary search problems!!!
    # if a[0] < a[1]
    # a[1] < a[2] ....
    # then all element in order
    def isValidBST(self, root):
       if not root: return True
       stack = deque()
       pre = None
       while root or stack:
          while root:
             stack.append(root)
             root = root.left

          root = stack.pop()
          if pre  and root.val <= pre.val: return False
          pre = root
          root = root.right

       return True

    # in order traversal - other approach
    def isValidBST2(self, root):
        if not root: return True
        stack = []
        res = []
        while root or stack:
            if root:
                stack.append(root)
                root = root.left
            else:
                root = stack.pop()
                res.append(root.val)
                root = root.right
        if res == sorted(res) and len(res) == len(set(res)):
            return True
        else:
            return False

root = Node(4)
root.left = Node(2)
root.left.left = Node(1)
root.left.right = Node(3)

print(Solution().validateBST(root))
print(Solution().isValidBST(root))

