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


# 책 풀이 - 반복구조
class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        if not head or m == n:
            return head

        root = start = ListNode(None)
        root.next = head

        for _ in range(m - 1):
            start = start.next
        end = start.next

        for _ in range(n - m):
            temp = start.next
            start.next = end.next
            end.next = end.next.next
            start.next.next = temp

        return root.next
# 우와 내 기준엔 이게 제일 어려운 것 같은데?
# .next가 포인터가 가리키는 '노드'를 의미하는지, 아니면 그 '화살표 자체'를 의미하는지가 가장 헷갈린다.
# 이 부분 개념을 제대로 알아야 temp 를 따로 만들어줄지 말지 결정을 내릴 수 있을 듯 함.









