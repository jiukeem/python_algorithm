# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# my solution
class Solution:
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        if root:
            if root.val == val:
                return root
            elif root.val < val:
                return self.searchBST(root.right, val)
            else:
                return self.searchBST(root.left, val)

        return None
# Status: Accepted
# Algorithm: Recursion
# Time Complexity: O(lg(n))
# Runtime: 108ms (top 71.5%)

class Solution:
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        iterator = root
        while iterator:
            if iterator.val == val:
                return iterator
            elif iterator.val < val:
                iterator = iterator.right
            else:
                iterator = iterator.left

        return None
# Status: Accepted
# Algorithm: Iteration
# Time Complexity: O(lg(n))
# Runtime: 80ms (top 26.8%)