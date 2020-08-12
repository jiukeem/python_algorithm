# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# value를 바꾸지 말고 노드 자체를 변경하라는 걸 보니 링크를 수정하라는 의도인 것 같다
# value를 변경하는 방법도 한번 해보기나 하자
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        node = head

        while node and node.next:
            node.val, node.next.val = node.next.val, node.val
            node = node.next.next

        return head
# 아 value를 변경하면 링크는 건드릴 필요도 없이 너무 간편해져서 문제의 의도랑 어긋나서 그렇구나.


# 책 풀이 - 반복구조
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        root = prev = ListNode(None)
        prev.next = head

        while head and head.next:
            b = head.next                  # b는 head의 링크가 가리키는 노드
            head.next = b.next             # head의 링크를 b의 링크, 즉 head의 다다음 노드로 변경
            b.next = head                  # b의 링크는 이제 head로 수정. b와 head의 순서가 바뀌었다.
            # 다중 할당으로는 안된다. 밑에 추가 설명 달아놓음
            prev.next = b                  # head의 앞 노드의 링크를 b로 수정해줌

            # 다음 단계로 이동
            head = head.next               # head는 이미 b와 자리가 바뀐 상태이므로 한칸만 이동
            prev = prev.next.next          # prev의 링크만 수정하고 prev 위치는 건드린 적이 없으므로 두칸 이동

        return root.next
# 와 너무 어렵당
# 일단 혼자 도전해봤을 때 prev 설정 부분에서 헤맸다.
# 움직이지 않는 root와 prev를 둬서 prev는 head와 함께 움직이며 swap을 수행하고
# 다 하고 나면 root.next로 새로운 head를 출력한다.
# root와 prev는 같은 값을 참조하고 있기 때문에 prev.next가 바뀌는 대로 root.next도 같은 값을 지닌다.
# 파이썬의 참조개념이 굉장히 헷갈리는데(할당과 다름) 그러면
# b = head.next \n head.next = b.next \n b.next = head 는 왜 잘 작동하느냐?
# 내 생각에는 얘네는 전부 새로운 값을 참조하도록 수정하는 개념이라서 그런 것 같다.
# 일단 b가 새로 생겨난 variable이기 때문에 다중할당으로 쓰면 에러가 난다. 오른쪽에 define 하지도 않은 b.next가 있으므로.
# 0234문제에서는 두 개의 variable이 같은 노드를 참조하고 있는 상태에서 걔의 메소드 값을 변경해준거라서
# 나머지 하나도 따라간거고, 여기서는 b를 head.next가 참조하고 있는 노드를 참조하게 한 다음에
# 두번째 줄에서는 head.next를 b.next가 참조하고 있는 노드(값)로 참조 위치를 변경한 개념으로 보면 될 것 같다.
# 세번째 줄도 마찬가지. 이게 굉장히 어렵고 헷갈린다ㅜㅜ
# 이 두 문제 가지고는 완전히 체득하기 어렵고 문제를 많이 풀다보면 감이 좀 잡힐 것 같다.


# 책 풀이 - 재귀 구조
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if head and head.next:
            p = head.next
            head.next = self.swapPairs(p.next)
            p.next = head
            return p

        return head
# 와... 이런생각은 어떻게 하시는거에요? 진짜 완벽해
# 처음에 보고 이게뭐야 했는데 노트에 찬찬히 풀어보니 군더더기가 하나도 없는 완벽한 풀이다
# 자 찬찬히 보자.
# [1 - 2 - 3 - 4 - 5 - 6] 연결리스트가 있다고 할 때
#
# 가장 바깥 함수)              head = 1, p = 2, 1.next = func(3)
# 함수 하나 안으로 들어감)           head = 3, p = 4, 3.next = func(5)
# 하나 더 안으로 들어감)                 head = 5, p = 6, 5.next = func(None) (6.next = None)
# 마지막으로 한번 더 재귀)                    head = None 이므로 return head=None
# 하나 바깥으로 나옴)                   5.next = None, 6.next = 5, return p=6
# 하나 더 바깥으로 나옴)            3.next = 6, 4.next = 3, return 4
# 가장 바깥으로 나옴)          1.next = 4, 2.next = 1, return 2
#
# 최종적으로 return 하는 것은 2고 변경된 연결리스트를 살펴보면
# [2 - 1 - 4 - 3 - 6 - 5]
# 정확!!!!! 너무 대단해. p.next를 먼저 변경해주지 않고 기존의 p.next를 이용해서
# 재귀함수를 먼저 실행시키는 것도 눈여겨봐야할 포인트
# root나 prev 같은 애들을 설정할 필요가 없어 공간사용이 효율적이다.



