# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# my solution
class Solution:
    def findTarget(self, root: TreeNode, k: int) -> bool:
        if root is None:
            return False

        self.BST = []
        def inorder(node):
            if node.left:
                inorder(node.left)
            self.BST.append(node.val)
            if node.right:
                inorder(node.right)

        inorder(root)
        start = 0
        end = len(self.BST) - 1
        while start < end:
            two_sum = self.BST[start] + self.BST[end]
            if two_sum == k:
                return True
            if two_sum < k:
                start += 1
            if two_sum > k:
                end -= 1

        return False
# Status: Accepted
# Algorithm: BST inorder traversal + two pointer
# Time Complexity: O(n)
# Runtime: 92ms (top 46.2%)


# leetcode discussion solution
class Solution:
    def findTarget(self, root: TreeNode, k: int) -> bool:
        if root is None:
            return False

        from collectinos import deque
        q = deque(root)
        seen = set()

        while q:
            node = q.leftpop()
            if node.val in seen:
                return True
            seen.add(k - node.val)
            if node.left: q.append(node.left)
            if node.right: q.append(node.right)

        return False
# Status: Accepted
# Algorithm: BFS search
# Time Complexity: O(n)
# Runtime: 72ms (top 5.1%)

