"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

# my solution
class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if root is None:
            return None

        from collections import deque
        q = deque()
        q.append(root)

        idx = 0
        while q:
            for _ in range(pow(2, idx)):
                first = q.popleft()
                if first is None:
                    return root
                first.next = q[0] if q else None
                q.append(first.left)
                q.append(first.right)
            first.next = None
            idx += 1

        return root
# Status: Accepted
# Algorithm: BFS
# Time Complexity: O(n)
# Runtime: 64ms (top 14.1%)
# Intuition: 포화이진트리이므로 큐를 쌓으면 2의 지수 개수만큼의 요소들이 같은 레벨임을 이용
#            root이 None인 경우를 예외처리 해줬으므로 q.popleft()가 None일 경우 트리가 끝난 것.

# 혼자서 '아 될 것 같은데-' 하면서 몇십분을 씨름하다가 풀었다. 너무 뿌듯해


# leetcode discussion solution
class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if root and root.left and root.right:
            root.left.next = root.right
            if root.next:
                root.right.next = root.next.left
            self.connect(root.left)
            self.connect(root.right)

        return root
# Status: Accepted
# Algorithm: Recursion
# Time Complexity: O(n)
# Runtime: 68ms (top 27.9%)
# 같은 O(n)이더라도 훨씬 간결하고 이해가 쉬운 코드. 완벽한 부분문제를 찾았다.