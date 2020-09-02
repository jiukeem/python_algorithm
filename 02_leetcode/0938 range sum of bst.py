# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# 릿코드 솔루션1 - 재귀구조
class Solution:
    def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:
        def dfs(node):
            if node:
                if L <= node.val <= R:
                    self.ans += node.val
                if L < node.val:
                    dfs(node.left)
                if R > node.val:
                    dfs(node.right)

        self.ans = 0
        dfs(root)
        return self.ans


# 릿코드 솔루션2
class Solution:
    def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:
        ans = 0
        stack = [root]
        while stack:
            node = stack.pop()
            if node:
                if L <= node.val <= R:
                    ans += node.val
                if L < node.val:
                    stack.append(node.left)
                if node.val < R:
                    stack.append(node.right)

        return ans

# 이제 트리,그래프 등 비선형구조 문제를 풀어야하는데 처음 접하다보니 감이 잘 안잡혀서 공부한 문제
# recursive나 iterative나 방식은 똑같다.
# 이 노드가 조건을 만족하면 총합변수에 더하고, L보다 크면 왼쪽노드를 다시 조사, R보다 작으면 오른쪽 노드를 다시 조사
# 이 세개가 elif가 아닌 if로, 조건만 만족하면 한 노드에 대해 세 연산이 다 수행될 수 있다.
# 나는 L따로 R따로 하면서 어떻게 똑같은 값을 두번 더하지 않을 수 있을까 고민했다(node.visited를 만들어줘야하나 했음)
# 그리고 dfs라는게 트리에서도 이렇게 자연스럽게 쓰이는 거구나.
# 이론을 배울 때 그래프에서 배웠는데 dfs는 굉장히 다양한 문제에서 쓰일 수 있는 알고리즘인 것 같다.