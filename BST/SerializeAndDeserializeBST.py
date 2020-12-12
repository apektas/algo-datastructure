class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

#https://leetcode.com/problems/serialize-and-deserialize-bst/discuss/177617/the-General-Solution-for-Serialize-and-Deserialize-BST-and-Serialize-and-Deserialize-BT

class Codec:

    def serialize(self, root: TreeNode) -> str:
        """Encodes a tree to a single string."""
        if not root: return ""
        stack, out = [root], []
        while stack:
            cur = stack.pop()
            out.append(cur.val)
            ## process left to right - pop manner
            for child in filter(None, [cur.right, cur.left]):
                stack.append(child)
        return ' '.join(map(str, out))

    def deserialize(self, data: str) -> TreeNode:
        """Decodes your encoded data to tree."""
        preorder = [int(i) for i in data.split()]
        def helper(up, down):
            if self.idx >=len(preorder): return None
            if not down <= preorder[self.idx] <=up: return None
            root = TreeNode(preorder[self.idx])
            self.idx +=1
            root.left = helper(down, root.val)
            root.right = helper(root.val, up)
            return root
        self.idx = 0
        return helper(float("-inf"), float("inf"))

    # this is more convenient way
    def deserializeII(self, data: str) -> TreeNode:
        values = collections.deque(int(val) for val in data.split())
        def deserializeHelper(lower, upper):
            if values and lower < values[0] < upper:
                value = values.popleft()
                node = TreeNode(value)
                node.left = deserializeHelper(lower, value)
                node.right = deserializeHelper(value, upper)
                return node
        return deserializeHelper(float("-inf"), float("inf"))

    def serializeTwo(self, root):
        values = []
        def preOrder(node):
            if root:
                values.append(root)
                preOrder(root.left)
                preOrder(root.right)
        preOrder(root)
        return ' '.join(map(str, values))


'''
     1
    / \
   3   4
  / \   \
 2   5   7
'''
tree = TreeNode(1)
tree.left = TreeNode(3)
tree.right = TreeNode(4)
tree.right.right = TreeNode(7)
tree.left.left= TreeNode(2)
tree.left.right = TreeNode(5)


codec = Codec()
print(codec.serialize(tree))