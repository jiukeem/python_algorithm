# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# leetcode discussion solution
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
        if preorder is None: return None
        root = TreeNode(preorder[0])
        stack = [root]
        for num in preorder[1:]:
            if num < stack[-1].val:
                stack[-1].left = TreeNode(num)
                stack.append(stack[-1].left)
            else:
                while stack and stack[-1].val < num:
                    last = stack.pop()
                last.right = TreeNode(num)
                stack.append(last.right)

        return root
# Status: Accepted
# Algorithm: stack
# Time Complexity: O(n)
# Runtime: 32ms (top 5.4%)
# 문제 자체를 이해 못해서 끙끙대다가 보고 공부했다.
# preorder traversal 같은 경우는 리스트로 주어지는 걸 보니 노드가 아니라 그냥 숫자값이 담긴 리스트로 보면 되겠다.
# else 부분에서 헷갈렸는데 preorder이기 때문에 계속 pop 해주는게 가능하다. 흠 어렵당