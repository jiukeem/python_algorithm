# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumRootToLeaf(self, root: TreeNode) -> int:
        stack = [(root, 0)]
        tot_sum = 0
        while stack:
            node, curr_num = stack.pop()
            if node:
                curr_num = (curr_num << 1) | node.val
                if node.left is None and node.right is None:
                    tot_sum += curr_num
                else:
                    stack.append((node.left, curr_num))
                    stack.append((node.right, curr_num))

        return tot_sum
# 릿코드 솔루션을 이해한 뒤에 다시 짜본 코드. 이진수를 다뤄본 적이 없어 비트연산자 등을 처음 써봤다.
# Status: Accepted
# Algorithm: DFS(with stack)
# Time Complexity: O(n)
# Runtime: 60ms (top 70.3%)
