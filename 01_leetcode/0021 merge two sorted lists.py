# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# 책 풀이: 재귀구조로 연결
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if (not l1) or (l2 and (l1.val > l2.val)):
            l1, l2 = l2, l1

        if l1:
            l1.next = self.mergeTwoLists(l1.next, l2)

        return l1
# 재귀구조를 처음 써봤다!
# 지금 하고 있는건 결국 l2를 l1으로 합치고 있는 과정
# 첫번째 if를 보면, l1이 끝났거나, l1이 l2보다 크면 l1과 l2를 뒤집어준다. 
# 즉, 현재의 l1 자리를 l2에게 내어준다.(l2가 작아서 앞에 들어가야 함)
# 다음 if를 보자. l1이 아직 남아있다면, 다음 노드를 l1으로 그대로 가지고 갈지,
# l2로 교체할지 다시 위의 과정을 반복해서 정해준다(재귀)
# 흠 근데 헷갈리는 건 첫 if문에서 (not l1.val) 이렇게 해줘야하는거 아닌가? 그 부분이 자꾸 헷갈린다.


# -----------------------------------------------------------------------------------------
# 0813(연결리스트 한번 훑기 완료한 날) 책 없이 나 혼자 다시 풀이 도전
# iteratively, not in-place
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        root = cur = ListNode(None)

        while l1 and l2:
            if l1.val < l2.val:
                cur.next = l1
                l1 = l1.next
            else:
                cur.next = l2
                l2 = l2.next

            cur = cur.next

        cur.next = l1 or l2
        return root.next
# ㅎㅎㅎ못품... 이건 누가 올려놓은 답 보고 적은거임
# 개념은 나도 똑같이 생각했는데 return 바로 위에 cur.next = l1 or l2
# 저런 코드가 되는구나. while 연산이 끝나고 난 후 l1, l2 중 남아있는 애들 갖다 붙이는 것.
# 책 풀이인 재귀는 더 명쾌하지만 내가 바로 저렇게 쓸 수 있는 능력이 안된다ㅜㅜ
# dummy가(임시 variable)이 있어도 일단은 이렇게만 풀 줄 알면 충분한 듯. 아 그리고 이건 in place가 아니다


# iteratively, in-place
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        root = cur = ListNode(None)
        cur.next = l1

        while l1 and l2:
            if l1.val < l2.val:
                l1 = l1.next
            else:
                temp = l2.next
                cur.next, l2.next = l2, l1
                l2 = temp
            cur = cur.next

        cur.next = l1 or l2
        return root.next
# 우왓 이건 내가 짠거!!!
# root도 있고 temp도 있지만 그래도 짤 수 있게 됐다!! 신나!
