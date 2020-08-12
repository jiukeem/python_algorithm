# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# one pass, 즉 시간복잡도 O(n)에 하라는 조건
# 내 풀이
class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        if not head:
            return None

        m_node = n_node = head
        for _ in range(n-1):
            n_node = n_node.next

        for _ in range(m - 1):
            m_node = m_node.next

        n_node.val, m_node.val = m_node.val, n_node.val
        return head
# 압 원패스도 아니고 문제를 잘못 이해했다. m과 n을 바꾸라는게 아니라 m부터 n까지를 뒤집으라는 얘기다
# 꼼수써서 val만 바꾸려다가 딱걸렸다.

