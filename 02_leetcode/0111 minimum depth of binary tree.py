# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# my solution
class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if root is None: return 0
        from collections import deque

        q = deque([root, 1])
        while q:
            node, curr_depth = q.popleft()
            if node:
                if node.left is None and node.right is None:
                    return curr_depth
                q.append((node.left, curr_depth+1))
                q.append((node.right, curr_depth+1))
# Status: Accepted
# Algorithm: BFS
# Time Complexity: O(n)
# Runtime: 48ms (top 37.6%)
