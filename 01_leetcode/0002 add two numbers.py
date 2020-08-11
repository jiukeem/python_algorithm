# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# 내 풀이 - 리스트로 변환해서 계산, 다시 연결리스트로 return
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:

        # 연결리스트를 리스트로 변환(reverse까지)
        def singlelinkToList(l: ListNode):
            lst = []
            while l:
                lst.append(l.val)
                l = l.next
            return reversed(lst)

        # 리스트를 숫자로 변환
        def listToInt(lst: List):
            num = int(''.join(str(i) for i in lst))
            # 이 부분 유의! 밑에 추가로 설명을 써놨다.
            return num

        # 리스트를 연결리스트로 변환
        def listToSinglelink(lst):
            prev: ListNode = None

            for i in lst:
                node = ListNode(i)
                node.next = prev
                prev = node
            return node

        l1_list = singlelinkToList(l1)
        l2_list = singlelinkToList(l2)

        l1_num = listToInt(l1_list)
        l2_num = listToInt(l2_list)

        sum = l1_num + l2_num
        sum_list = [int for int in str(sum)]

        return listToSinglelink(sum_list)
# runtime 상위 10프로
# 책에도 같은 풀이가 있는데 list -> singlelink 함수는 구현이 어려워서 책을 보고 했다
# 나머지는 내가 작성!
# 이 코드는 연결리스트를 리스트로 변형한 뒤 다시 연결리스트로 바꾸는 풀이라서
# 잘못된 건 아니지만 추천할만한 풀이는 또 아니다.


# 책 풀이 - 전가산기 구현
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        root = head = ListNode(0)

        carry = 0
        while l1 or l2 or carry:
            sum = 0

            if l1:
                sum += l1.val
                l1 = l1.next

            if l2:
                sum += l2.val
                l2 = l2.next

            carry, val = divmod(sum + carry, 10)
            head.next = ListNode(val)
            head = head.next

        return root.next
# 논리 회로에 대해서는 잘 모르지만 이 풀이의 원리는 아주 간단하다.
# carry 라는 변수를 만들어서 l1과 l2 의 합이 10이 넘을 경우 1을 지니고 다음 계산으로 넘겨준다.
# 그리고 root 라는 변수를 만든 것도 눈여겨 볼 점이다.
# 내가 작성한 코드에서 listToSinglelink(lst) 를 짤 때,
# 처음 -> 끝 순서로 노드를 추가하니 head 를 return 할 방법이 없어서 head에서 node가 끝나도록 반대 방향으로 짰었다.
# 여기서는 head와 별개로 root를 둬서 root.next 를 통해 바로 head 로 넘어갈 수 있도록 했다. (head는 이미 맨끝 노드까지 간 상태)
# 나도 다음에 이렇게 짜야징!



# 숫자형 리스트를 단일 값으로 병합하기 에 대한 추가 설명
'''
num = int(''.join(str(i) for i in lst)) 이 부분에 대한 설명이다. 
int로 구성된 리스트를 하나씩 꺼내면서 str으로 바꿔준 뒤 합치고 그걸 다시 int 시키는게 굉장히 비효율적이다.
우선 가장 쉬운 개선방법은 리스트 컴프리헨션 대신 map(str, lst)를 쓰는 것으로, 훨씬 간결해진다.
책에서는 str형식을 거치지 않고 처리할 수 있는 방법을 추가로 소개한다.

>>> functools.reduce(lambda x, y: 10 * x + y, a, 0)

functools는 함수형 언어 모듈로, 다른 함수에 작용하거나 다른 함수를 반환하는, 함수를 다루는 함수다.
functools.reduce 는 두 인수의 함수를 누적 적용하는 메소드다. 
예를 들어 functools.reduce(lambda x, y: x + 2* y, [1, 2, 3, 4, 5]) 는
(((1 + 4) + 6) + 8) + 10 = 29 가 된다.
즉, 위의 식을 보면 x에 10을 곱하고 y를 일의자리로 더한다. 그리고 걔네에 10을 곱하고 다음 y를 일의자리에 더해준다.
굉장히 직관적이고 멋진 방식이다. 이해하긴 했는데 도움없이 나 혼자 쓸 수 있을지는...
'''
