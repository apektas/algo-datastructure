class TreeNode:
    def __init__(self, val, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

class Solution:
    def __init__(self, root):
        self.root = root

    def populateNextRight(self, root):
        from collections import deque
        if not root: return root
        queue = deque()
        queue.append(root)
        while queue:
            N = len(queue)
            node = queue.popleft()
            if node.left: queue.append(node.left)
            if node.right: queue.append(node.right)
            for i in range(1, N):
                nextNode = queue.popleft()
                node.next = nextNode
                node  = nextNode
                if node.left: queue.append(node.left)
                if node.right: queue.append(node.right)
            node.next = None
        return root


