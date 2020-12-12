class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


from collections import deque
class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root: return root
        queue = deque()
        queue.append(root)
        while queue:
            N = len(queue)
            node = queue.popleft()
            if node.left: queue.append(node.left)
            if node.right: queue.append(node.right)
            for i in range(1,N):
                nextNode = queue.popleft()
                node.next = nextNode
                node=nextNode
                if node.left: queue.append(node.left)
                if node.right: queue.append(node.right)
            node.next=None

        return root
