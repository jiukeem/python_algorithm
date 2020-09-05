# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# my solution
class Solution:
    def maxLevelSum(self, root: TreeNode) -> int:
        from collections import deque
        from collections import defaultdict

        q = deque([(root, 1)])
        level_sum = defaultdict(int)

        while q:
            node, level = q.popleft()
            if node:
                level_sum[level] += node.val
                q.append((node.left, level + 1))
                q.append((node.right, level + 1))

        tot = - sys.maxsize
        for i in range(len(level_sum), 0, -1):
            if level_sum[i] >= tot:
                tot = level_sum[i]
                res = i

        return res
# Status: Accepted
# Algorithm: BFS
# Time Complexity: O(n)
# Runtime: 360ms (top 43.6%)



