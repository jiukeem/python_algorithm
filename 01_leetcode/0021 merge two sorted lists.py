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
