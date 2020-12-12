class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def inOrderTraversal(self, root):

        res, stack = [], []
        cur = root
        while cur or stack:
            while cur:  # travel to each node's left child, till reach the left leaf
                stack.append(cur)
                cur = cur.left
            cur = stack.pop()  # this node has no left child
            res.append(cur.val)  # so let's append the node value
            cur = cur.right  # visit its right child -->
                            # if it has left child ? append left and left.val,
                            # otherwise append node.val,
                            # then visit right child again... cur = node.right
        return res

root = TreeNode(3)
root.left = TreeNode(8)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)

print(Solution().inOrderTraversal(root))