# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# leetcode discussion solution
class Solution:
    def findSecondMinimumValue(self, root: TreeNode) -> int:
        self.sec_min = sys.maxsize

        def traverse(node):
            if node:
                if node.val > root.val:
                    self.sec_min = min(self.sec_min, node.val)
                traverse(node.left)
                traverse(node.right)

        traverse(root)
        return -1 if self.sec_min == sys.maxsize else self.sec_min
# Status: Accepted
# Algorithm:
# Time Complexity: O(n)
# Runtime: 32ms (top 35.6%)
# 문제 자체가 좀 별로인 것 같다. 비추수가 많은 문제는 이유가 있는듯..
# 효율적으로 풀려고 엄청 애썼는데 결국 n개를 traverse할 수 밖에 없는 예외 예제들이 뜨더라.