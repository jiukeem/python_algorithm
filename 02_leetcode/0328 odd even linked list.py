# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# 시간복잡도 O(n), 공간복잡도 O(1)에 풀이하라는 조건

# 책 풀이 - 반복구조 이용
class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        # 예외처리
        if not head:
            return None

        odd = head
        even = head.next
        even_head = head.next
        # 마지막에 홀수리스트의 끝과 이어줄 때 짝수리스트의 첫 노드가 필요하므로 even_head를 별도로 생성

        while even and even.next:
            odd.next, even.next = odd.next.next, even.next.next
            odd, even = odd.next, even.next

        odd.next = even_head
        return head
# 처음에 든 생각은 이거 홀수리스트랑 짝수리스트를 따로 만들어 나가는데 그럼 공간복잡도 O(1)이 아닌거 아냐?
# 음 근데 생각해보면 O(1)이라는게 output말고 다른 변수가 없게하라- 이게 아니라
# n(여기서는 노드 개수)에 상관없이 일정하게 사용하는 것을 말하기 때문에
# odd, even, even_head는 n의 크기에 관계없이 항상 일정하게 사용하고 있으므로 만족한다.
# 그리고 홀수/짝수리스트도 기존의 n을 반 쪼개서 할당한 것이므로 공간차지가 늘어나지 않는다.
# 맨 처음부터 뒤로 쭉 지나가면서 홀수/짝수리스트를 동시에 생성하므로 시간복잡도도 O(n)이다.
# 음 코드 짜는건 그렇게 어렵지 않았다. 근데 홀수/짝수를 따로 만들어 나가야겠다는 아이디어를 떠올리지 못하니
# 링크가 유실되면 다음 애를 찾을 수가 없으니까 이 링크를 어디다가 임시로 연결해놔야하지? 하면서 점점 복잡해졌다.





