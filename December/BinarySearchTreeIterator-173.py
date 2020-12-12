# Definition for a binary tree node.
from collections import deque
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class BSTIterator:

    def __init__(self, root: TreeNode):
        self.stack = deque()
        curNode = root
        self._partialInOrder(curNode)

    # push left
    def _partialInOrder(self, node: TreeNode):
        while node:
            self.stack.append(node)
            node = node.left

    def next(self) -> int:
        node = self.stack.pop()
        # process right subTree
        self._partialInOrder(node.right)
        return node.val

    def hasNext(self) -> bool:
        return self.stack and len(self.stack)>0

# good explanation
# https://www.youtube.com/watch?v=C8iHdhXjKC4
# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()