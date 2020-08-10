# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# 리스트로 변경해서 푸는 방식
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        if head is None:
            return True

        lst = []
        while head is not None:
            lst.append(head.val)
            head = head.next

        while len(lst) > 1:
            if lst.pop(0) != lst.pop():
                return False

        return True
# 리스트로 바꾸면 pop을 이용해서 비교는 편하게 할 수 있으나,
# 모든 요소를 순서대로 리스트에 넣어줘야하기 때문에 runtime이 길다 (하위 5프로)
# 아 속도 문제는 저 부분보다 pop에서 발생한다고 한다.
# 리스트는 동적배열로 구성된 리스트여서 맨 앞 아이템을 가져오기 적합한 자료형이 아니다.
# 맨 앞의 값을 꺼내올 때 모든 값이 한 칸씩 당겨지며 시간복잡도가 O(n)이다.
# 파이썬의 데크deque는 이중 연결리스트 구조이기 때문에 양쪽 방향 모두 추출하는 데 시간복잡도 O(1)이다.
# (근데 이중 연결이 아니더라도 그냥 연결리스트라면 O(1) 아닌가? 이중 연결이면 탐색시간이 줄어드는거고.)
# 데크는 아직 안배웠기 때문에 두번째 풀이 방법은 나중에 해보자~


# runner를 이용한 풀이 방식
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        rev = None
        # rev에도 None을 넣어줘야한다. 마지막 노드의 .next 가 None 이니까.
        # 만약 안넣을거라면 마지막 return에 not slow만 쓸 수 있다(not rev 는 불가능)
        slow = fast = head
        # 둘 다 0번 인덱스에서 시작

        while fast and fast.next:
            fast = fast.next.next
            # fast는 두칸씩 나가며(slow 의 두배) 연결리스트의 개수가 짝수인 경우 None으로 끝나게 된다.
            rev, rev.next, slow = slow, rev, slow.next
            # 이 부분 유의! 다줄 할당 개념에 유의하기
            # 이 부분을 두 줄에 나눠서 rev, rev.next 와 slow 를 따로 쓰면
            # rev가 slow에 할당되어 있는 상태에서 rev.next를 수정하므로
            # slow.next 도 앞으로 가는게 아니라 rev 연결리스트를 따라서 같이 뒤로 이동해버린다
            # 파이썬은 모든 변수들이 참조를 할당받는 객체 방식이라 그렇다.

        if fast:
            slow = slow.next
            # if fast 는 연결리스트의 개수가 홀수 개일 경우 와 같은 말이며
            # 홀수일 경우 가운데 노드는 제외하고 slow와 rev를 비교해야하기 때문에
            # slow를 한개 넘겨주는 것.

        while rev and rev.val == slow.val:
            slow, rev = slow.next, rev.next
            # rev의 값이 있고 rev와 slow의 값이 같다면 다음으로 넘어간다
            # rev는 중앙에서 앞으로 돌아가고 slow는 중앙에서 뒤로 가므로
            # 펠린드롬이라면 두 개가 전부 None에 도달해야할 때까지 진행되어야 한다.

        return not rev
        # rev 가 None 이면 True

# 와 runner 어렵다! 근데 정말 합리적이고 똑똑한 방식이다.
# 지금은 runner 개념 뿐만 아니라 연결리스트가 익숙지않아서 좀 더 어렵게 느껴질 수 있는데
# 여러번 써보면 금방 손에 익을 것 같다.
# runtime 상위 2퍼센트에 memory usage 상위 9프로다.. 짱짱