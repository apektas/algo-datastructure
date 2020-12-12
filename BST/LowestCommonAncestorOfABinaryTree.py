# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def dfs(node):
            ## if Node is None or val equals to p or q then return node
            if node in (None, p, q): return node
            left = dfs(node.left)
            right = dfs(node.right)
            # if return of left and right exists then return that node
            if left and right: return node
            # otherwise return node!=None
            if left: return left
            if right: return right
        return dfs(root)

    '''
        def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        """
        Approach 2: bfs
        time complexity: O(n)
        space complexity: O(n)
        """
        queue = collections.deque([root])
        parent = {root: None}
        
        while p not in parent or q not in parent:
            node = queue.popleft()
            if node.left:
                parent[node.left] = node
                queue.append(node.left)
            if node.right:
                parent[node.right] = node
                queue.append(node.right)
        
        ancestors = set()
        while q:
            ancestors.add(q)
            q = parent[q]
            
        while p not in ancestors:
            p = parent[p]
            
        return p
    '''

# https://www.youtube.com/watch?v=0hTLjO5CENQ

'''
       3
      / \
     6   8
    / \   \
   2  11   13
      / \  /
     9   5 7
'''
root = TreeNode(3)
root.left = TreeNode(6)
root.left.left = TreeNode(2)
root.left.right = TreeNode(11)
root.left.right.left = TreeNode(9)
root.left.right.right = TreeNode(5)

root.right = TreeNode(8)
root.right.right = TreeNode(13)
root.right.right.left=TreeNode(7)

# https://www.youtube.com/watch?v=13m9ZCB8gjw&t=1s
# 8, 7
print(Solution().lowestCommonAncestor(root, root.right, root.right.right.left).val) # return 8
assert 8 == Solution().lowestCommonAncestor(root, root.right, root.right.right.left).val, "Failed"

# 2, 5
print(Solution().lowestCommonAncestor(root, root.left.left, root.left.right.right).val) # return 8
assert 6 == Solution().lowestCommonAncestor(root, root.left.left, root.left.right.right).val, 'Failed 2, 5'

