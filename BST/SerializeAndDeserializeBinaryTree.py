# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:

    # pre-order traversal
    def serialize(self, root):
        """Encodes a tree to a single string."""

        if not root: return "#"
        result = ''
        result += str(root.val)
        result += "," + self.serialize(root.left)
        result += "," + self.serialize(root.right)
        return result

    def deserialize(self, data):
        """Decodes your encoded data to tree."""
        def deserializeHelper(values):
            value = next(values)
            if value == "#":
                return None
            node = TreeNode(int(value))
            node.left = deserializeHelper(values)
            node.right = deserializeHelper(values)
            return node

        values = iter(data.split(','))
        return deserializeHelper(values)



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



# Your Codec object will be instantiated and called as such:
ser = Codec()
print(ser.serialize(tree))
deser = Codec()
deser.deserialize(ser.serialize(tree))
# ans = deser.deserialize(ser.serialize(root))