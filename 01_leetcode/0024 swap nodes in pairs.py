# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# value를 바꾸지 말고 노드 자체를 변경하라는 걸 보니 링크를 수정하라는 의도인 것 같다
# 책 풀이 - 재귀구조
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        root = prev = ListNode(None)
        prev.next = head

        while head and head.next:
            b = head.next
            head.next = b.next
            b.next = head
            # 놀랍게도 다중할당과 연관이 없다!


# value를 변경하는 방법도 한번 해보기나 하자
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        node = head

        while node and node.next:
            node.val, node.next.val = node.next.val, node.val
            node = node.next.next

        return head
# 아 value를 변경하면 링크는 건드릴 필요도 없이 너무 간편해져서 문제의 의도랑 어긋나서 그렇구나.


