from typing import List
from collections import deque
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def rangeSumBST(self, root: TreeNode, low: int, high: int) -> int:
        if not root: return 0
        result = 0
        queue = deque()
        queue.append(root)
        while queue:
            node = queue.popleft()
            if node.val >=low and node.val <= high: result+=node.val
            if node.left and node.val>low: queue.append(node.left)
            if node.right and node.val<high : queue.append(node.right)
            #
            # if node.val >= low and node.left: queue.append(root.left)
            # if node.val <= high and node.right: queue.append(root.right)

        return result

root = TreeNode(10)
root.left = TreeNode(5)
root.right = TreeNode(15)
root.right.right = TreeNode(18)
root.left.right = TreeNode(7)
root.left.left = TreeNode(3)

print(Solution().rangeSumBST(root,7,15))

# https://leetcode.com/problems/range-sum-of-bst/discuss/192019/JavaPython-3-3-similar-recursive-and-1-iterative-methods-w-comment-and-analysis.

'''
One way to solve this problem is just iterate over our tree and for each element check if it is range or not. However here we are given, that out tree is BST, that is left subtree is always lesser than node lesser than right subtree. So, let us modify classical dfs a bit, where we traverse only nodes we need:

Check value node.val and if it is in our range, add it to global sum.
We need to visit left subtree only if node.val > low, that is if node.val < low, it means, that all nodes in left subtree less than node.val, that is less than low as well.
Similarly, we visit right subtree only if node.val < high.
Complexity: time complexity is O(n), where n is nubmer of nodes in our tree, space complexity potentially O(n) as well. We can impove our estimations a bit and say, that time and space is O(m), where m is number of nodes in our answer.

class Solution:
    def rangeSumBST(self, root, low, high):
        def dfs(node):
            if not node: return
            if low <= node.val <= high: self.out += node.val
            if node.val > low:  dfs(node.left)
            if node.val < high: dfs(node.right)
                
        self.out = 0
        dfs(root)
        return self.out

'''

