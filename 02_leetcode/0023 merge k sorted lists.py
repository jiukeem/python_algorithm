# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# 책 풀이 - 힙을 이용한 우선순위 큐 사용
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        root = result = ListNode(val=None)
        heap = []

        for i in range(len(lists)):
            if lists[i]:
                heapq.heappush(heap, (lists[i].val, i, lists[i]))

        while heap:
            node = heapq.heappop(heap)
            idx = node[1]
            result.next = node[2]

            result = result.next
            if result.next:
                heapq.heappush(heap, (result.next.val, idx, result.next))

        return root.next
# 우선 root 와 result 노드를 만들어줬다. result는 계속 업데이트 되므로 자리를 지키고 있을 root가 필요하다
# lists를 돌면서 각 연결리스트의 첫번째 노드들을 노드의 val을 우선순위로 하여 heap에 추가한다. (lists 안의 연결리스트는 변하지 않음)
# 중간에 i값을 가지고 있는 이유는 같은 val을 가진 노드 두개가 들어오면 중복된 값이 추가됐다고 에러가 나기 때문에
# 구분하기 위해 i라는 인자 하나를 더 넣어준 것이다.

# heap이 있는 동안(heap이 비었으면 전부다 처리한 것이다)
# 가장작은 요소를 node로 빼고 result.next를 해당 노드로(node의 두번째 인덱스) 변경하고 result를 result.next로 옮긴다.
# 만약 result.next가 있다면, 즉 lists안에 이 노드가 있던 연결리스트의 뒷부분이 남아있다면
# 걔를 데려와서 다시 힙에 넣어준다. (lists안에 있는 모든 연결리스트들의 첫번째 노드들이 힙에 들어와있어야 제대로 비교할 수 있으므로)
# heap이 더이상 존재하지 않는다면, 모든 연결리스트들이 다 힙으로 들어왔고,
# 또 전부 우선순위 비교를 통해 result.next로 들어갔다는 뜻이므로 연산을 종료하고 root.next를 return한다.


# 책풀이 공부한거 안보고 다시 한 번 써보기
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        root = result = ListNode(val=None)
        heap = []

        for i in range(len(lists)):
            heapq.heappush(heap, (lists[i].val, i, lists[i]))

        while heap:
            info = heapq.heappop(heap)
            idx = info[1]
            result.next = info[2]
            result = result.next
            if result.next:
                heapq.heappush(heap, (result.next.val, idx, result.next))

        return root.next
# if lists[i] 부분, 즉 예외처리 부분을 빼고는 올바르게 썼다. 제대로 이해한 것 같다.

