# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        if root is None: return None
        stack = [(root, root.val, [root.val])]
        res = []
        while stack:
            last = stack.pop()
            left, right = last[0].left, last[0].right
            if last[1] == sum and left is None and right is None:
                res.append(last[2])
            if left:
                stack.append((left, last[1] + left.val, last[2] + [left.val]))
            if right:
                stack.append((right, last[1] + right.val, last[2] + [right.val]))

        return res

# Status: Accepted
# Algorithm: DFS
# Time Complexity: O(n)
# Runtime: 44ms (top 13.0%)
# Intuition: dfs로 내려가다가 leaf node이고 총합이 sum과 같으면 result 리스트에 추가.
#            leaf node나 path 개수가 아닌 path를 return 해야 하기 때문에 스택에 path 변수 추가