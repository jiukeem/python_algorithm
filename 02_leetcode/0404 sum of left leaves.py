# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# my solution
class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        if root is None:
            return 0

        from collections import deque
        q = deque([root])
        tot_sum = 0
        while q:
            node = q.popleft()
            if node:
                if node.left and node.left.left is None and node.left.right is None:
                    tot_sum += node.left.val
                elif node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

        return tot_sum
# Status: Accepted
# Algorithm: BFS
# Time Complexity: O(n)
# Runtime: 32ms (top 24.6%)

