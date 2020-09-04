# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# my solution
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        self.trav = []

        def inorder(node):
            if node:
                inorder(node.left)
                self.trav.append(node.val)
                inorder(node.right)

        inorder(root)
        return self.trav
# Status: Accepted
# Algorithm: recursion
# Time Complexity: O(n)
# Runtime: 24ms (top 5.1%)


# leetcode discussion solution
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        stack = []
        trav = []

        curr_node = root
        while (curr_node or stack):
            while curr_node:
                stack.append(curr_node)
                curr_node = curr_node.left

            last = stack.pop()
            trav.append(last.val)
            if last.right:
                curr_node = last.right

        return trav
# Status: Accepted
# Algorithm: iteration
# Time Complexity: O(n)
# Runtime: 32ms (top 46.8%)
# Intuition: inorder이므로 left를 넣어주고 pop하면서 right를 넣어준다.
#            나는 처음에 타임아웃이 발생했는데 이미 거쳐간 노드라도 left가 있다고 판단되서 다시 스택에 들어갔기 때문.
#            해결 방법으로는 위처럼 while문을 하나 더 넣거나 visited 변수를 추가해서 set로 스택에 추가하는 방법이 있다.