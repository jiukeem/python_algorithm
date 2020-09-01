# 시간복잡도가 O(n lg(n)) 이내일 것을 요구한다.
# 알파벳 별 출현 빈도수 딕셔너리를 생성하는 건 O(n)이므로
# 결국 dict를 어떻게 정렬할거냐는 문제.
# k는 최대 n이므로 그냥 for문으로 탐색하면 O(n^2)다.

# 내 풀이
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = collections.defaultdict(int)
        for num in nums:
            freq[num] += 1

        heap = []
        for key, value in freq.items():
            heapq.heappush(heap, (-value, key))

        sorted_list = []
        for _ in range(k):
            sorted_list.append(heapq.heappop(heap)[1])

        return sorted_list
# 힙정렬을 사용했다.(시간복잡도 O(n lg(n))) 우선순위와 내가 원하는 값이 따로 있으니까 이게 적합할 것 같아서~.~
# runtime 상위20프로 memory usage 상위5프로! 띠용 너무 잘했다.
# 책풀이도 힙정렬을 사용했다.




