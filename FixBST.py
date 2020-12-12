# class to store a Binary Tree node:
class Node:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


# Function to perform in-order traversal of the tree
def inorder(root):

    if root is None:
        return

    inorder(root.left)
    print(root.data, end=' ')
    inorder(root.right)


# Function to exchange data of given linked list nodes
def swapData(first, second):

    data = first.data
    first.data = second.data
    second.data = data


# Recursive function to insert a key into BST
def insert(root, key):

    # if the root is None, create a node and return it
    if root is None:
        return Node(key)

    # if given key is less than the root node, recur for left subtree
    if key < root.data:
        root.left = insert(root.left, key)

    # if given key is more than the root node, recur for right subtree
    else:
        root.right = insert(root.right, key)

    return root


# Recursive function to fix a binary tree that is only one swap
# away from becoming a BST. Here, prev is previous processed node in
# in-order traversal and x, y stores node to be swapped (if any)
def correctBST(root, x, y, prev):

    # base case
    if root is None:
        return x, y, prev

    # recur for left subtree
    x, y, prev = correctBST(root.left, x, y, prev)

    # if current node is less than the previous node
    if root.data < prev.data:
        # if this is first occurrence, update x and y to previous node
        # and current node respectively
        if x is None:
            x = prev

        # if this is second occurrence, update y to current node
        y = root

    # update previous node and recur for right subtree
    prev = root
    return correctBST(root.right, x, y, prev)


# Fix given binary tree that is only one swap away from becoming a BST
def fixBST(root):

    # x and y stores node to be swapped

    # stores previous processed node in in-order traversal
    # initialize it by minus infinity
    prev = Node(float('-inf'))

    # fix the binary tree
    x, y, prev = correctBST(root, None, None, prev)

    # swap the nodes data
    if x and y:
        swapData(x, y)


if __name__ == '__main__':

    """ Construct below BST
              15
            /    \
           /      \
          10       20
         /  \     /  \
        /    \   /    \
       8     12 16    25
    """

    keys = [15, 10, 20, 8, 12, 16, 25]

    root = None
    for key in keys:
        root = insert(root, key)

    # swap any two nodes values
    swapData(root.left, root.right.right)

    # fix the BST
    fixBST(root)

    # print the BST after fixing it
    inorder(root)
