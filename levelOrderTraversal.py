class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# https://leetcode.com/problems/binary-tree-level-order-traversal/discuss/114449/A-general-approach-to-level-order-traversal-questions-in-Java
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        result = []
        self.traversalHelper(root, result, 1)
        return result


    def traversalHelper(self, root, result, level):
        if(root is None): return
        if(len(result) < level):
            result.append([])
        result[level-1].append(root.val)
        if root.left: self.traversalHelper(root.left, result, level+1)
        if root.right: self.traversalHelper(root.right, result, level+1)


    def levelOrderTraversalIterative(self, root):
        if not root : return []
        queue, result = [root], []

        while queue:
            tmp = []
            N = len(queue)
            for i in range(N):
                node = queue.pop(0)
                tmp.append(node.val)
                if node.left: queue.append(node.left)
                if node.right: queue.append(node.right)
            result.append(tmp)
        return result

    def levelOrderTraversalBottom(self, root):
        if not root: return []
        from collections import deque
        # In Python, there’s a specific object in the collections module that you can use
        # for linked lists called deque (pronounced “deck”), which stands for double-ended queue.
        """
        >>> llist = deque("abcde")
        >>> llist
        deque(['a', 'b', 'c', 'd', 'e'])
        
        >>> llist.append("f")
        >>> llist
        deque(['a', 'b', 'c', 'd', 'e', 'f'])
        
        >>> llist.pop()
        'f'
        
        >>> llist
        deque(['a', 'b', 'c', 'd', 'e'])
        """
        #Both append() and pop() add or remove elements from the right side of the linked list.
        # However, you can also use deque to quickly add or remove elements from the left side, or head, of the list:
        # via appendleft and popleft
        result = deque() # popLeft -> insert into the beginning
        queue = [root]
        while queue:
            tmp = []
            N = len(queue)
            for i in range(N):
                node = queue.pop(0)
                if node.left: queue.append(node.left)
                if node.right : queue.append(node.right)
                tmp.append(node.val)
            result.appendleft(tmp) # since the deque is linkedlist, adding and removing element is fairly simple O(1) time complexity
        return list(result)
        ## or reverse the previous solution

    def zigzagTraversal(self, root):
        result = []
        if not root: return result
        leftToRight = True
        queue = [root]
        while queue:
            tmp =[]
            N = len(queue)
            for i in range(N):
                node = queue.pop(0)
                tmp.append(node.val)
                if node.left: queue.append(node.left)
                if node.right: queue.append(node.right)
            if leftToRight:
                result.append(tmp)
            else:
                result.append(tmp[::-1])
            leftToRight = not leftToRight
        return result

    def rightSideOfTheTree(self, root):
        if not root: return []
        result = []
        queue = [root]
        while queue:
            tmp = []
            N = len(queue)
            for i in range(N):
                node = queue.pop(0)
                tmp.append(node.val)
                if node.left: queue.append(node.left)
                if node.right: queue.append(node.right)

            result.append(tmp.pop())

        return result

    def averageOfLevelsInBT(self, root):
        if not root: return []
        result = []
        queue = [root]
        while queue:
            sum, tmp = 0, []
            N = len(queue)
            for i in range(N):
                node = queue.pop(0)
                sum += node.val
                if node.left: queue.append(node.left)
                if node.right: queue.append(node.right)
            result.append(sum/N)

        return result

    def findLargestValueInEachTreeRow(self, root):
        if not root: return []
        result = []
        queue = [root]

        while queue:
            maxVal = queue[0].val
            N = len(queue)
            for i in range(N):
                node = queue.pop(0) ## get first index works like queue
                maxVal = max(maxVal, node.val)
                if node.left: queue.append(node.left)
                if node.right: queue.append(node.right)
            result.append(maxVal)
        return result

    def populatingNextRightPointersInEachNode(self, root):
        if not root: return root
        queue = [root]

        while queue:
            N = len(queue)
            tmp = []
            for i in range(N):
                node = queue.pop(0)
                tmp.append(node)
                if node.left: queue.append(node.left)
                if node.right: queue.append(node.right)
            for i in range(N-1):
                node.right = tmp[i+1]
            node.right = None

        return root


#[3, [9,20] [15,7]]
  #   3
  #  / \
  # 9  20
  #   /  \
  #  15   7

root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)

root.right.left = TreeNode(15)
root.right.right = TreeNode(7)

#print(Solution().levelOrder(root))
print(Solution().levelOrderTraversalIterative(root))
print(Solution().levelOrderTraversalBottom(root))
print(Solution().zigzagTraversal(root))
print(Solution().rightSideOfTheTree(root))
print(Solution().averageOfLevelsInBT(root))
print(Solution().findLargestValueInEachTreeRow(root))
