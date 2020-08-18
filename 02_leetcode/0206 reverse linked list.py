# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# 책 풀이 - 재귀 구조 사용
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        def reverse(node: ListNode, prev: ListNode =None):
            if not node:
                return prev

            next_node, node.next = node.next, prev
            # 다중 할당을 사용한 부분. 두 줄로 나눠 작성했다면 제대로 작동하지 않았을거다.
            # next_node는 계속 뒤로 넘어가야하니 기존의 node.next를 할당해주어야 하고
            # 동시에 node.next는 prev로 변경해주어야 한다.
            return reverse(next_node, node)

        return reverse(head)
# 연결리스트는 재귀구조 및 다중할당과 함께 사용되는 경우가 많은 것 같다.
# 내용은 간단하고 직관적이어서 이해하기는 어렵지않지만 이 코드를 혼자서도 짤 수 있어야 한다.


# 책 풀이 - 반복 구조 사용
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        node, prev = head, None

        while node:
            next_node, node.next = node.next, prev
            node, prev = next_node, node

        return prev
# 사실 개념은 똑같다. 구조를 어떤 것을 사용하냐의 차이일 뿐.
# 다만 이경우, 나는 return prev가 헷갈렸다.
# 직접 노트에 연산 과정을 풀어써보고 나서야 그렇구나- 했다.
# 두 방식의 속도는 거의 비슷하며, memory usage는 반복구조가 좀 더 낮다.
# 나는 반복 구조가 더 잘 읽히는 것 같다.


# -----------------------------------------------------------------------------------------
# 0813(연결리스트 한번 훑기 완료한 날) 책 없이 나 혼자 다시 풀이 도전
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if not head:
            return None

        root = ListNode(None)
        root.next = head

        while head.next:
            nxt = head.next
            root.next, nxt.next, head.next = nxt, root.next, head.next.next

        return root.next
# 세상에세상에~~~ 너무 행복해~~~~ 너무 잘돌아간다(runtime, memory 똑같음!)~~~
# 코드는 조금 지저분할지 몰라도 내가 제대로 이해하고 있다는 거잖아! >_< 뿌듯
# 이제 조금씩조금씩 다듬어주면서 어떻게 더 간결하고 명확하게 짤 수 있을까 생각해보자


