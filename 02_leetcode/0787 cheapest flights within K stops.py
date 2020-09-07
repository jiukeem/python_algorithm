# 방향, 양수가중치 그래프

# my solution
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, K: int) -> int:
        from collections import defaultdict
        edges = defaultdict(list)
        for s, d, p in flights:
            edges[s].append((d, p))

        stops = [-1] * n
        completed = [0] * n
        prices = [sys.maxsize] * n

        s = src
        prices[s] = 0
        stops[s] = -1
        while True:
            for d, p in edges[s]:
                if completed[d] == 0 and stops[d] < K and (prices[s] + p) < prices[d]:
                    prices[d] = prices[s] + p
                    stops[d] = stops[s] + 1
            completed[s] = 1
            next_s = -1
            for num in range(n):
                if completed[num] == 0 and stops[num] <= K and prices[num] != sys.maxsize:
                    if next_s < 0 or (0 <= next_s and prices[num] < prices[next_s]):
                        next_s = num
            if next_s < 0:
                break
            s = next_s

        if completed[dst] == 0:
            return -1
        return prices[dst]
# Status: Wrong Answer
# Algorithm: Dijkstra
# Time Complexity: O(N^2 + E) (E: num of edges)
# Runtime:
# Intuition: 테스트케이스들을 해보다가 다익스트라로 안되는 부분 발견. DFS로 해야할 것 같다.
# 문제가 생긴 케이스 :4 [[0,1,1],[1,2,1],[0,2,5],[2,3,1]] 0 3 1
# 0 - 2 - 3 의 경로가 가능한데 2에는 0 - 1 - 2의 루트밖에 저장되어있지않다. (K조건을 충족시키는 가장 작은 값이기 때문에)

# leetcode discussion solution
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, K: int) -> int:
        from collections import defaultdict
        edges = defaultdict(dict)
        for s, d, p in flights:
            edges[s][d] = p
        heap = [(0, src, K + 1)]
        # (price(=path), node, left num of stops) -> 우선순위는 낮은 가격순?
        while heap:
            p, i, k = heapq.heappop(heap)
            if i == dst:
                return p
            if k > 0:
                # 아직 들를 수 있는 stop 개수가 남았을 경우
                for j in edges[i]:
                    heapq.heappush(heap, (p + edges[i][j], j, k - 1))
                    # 기존의 price와 min을 비교하지 않고 다 저장

        return -1
# Status: Accepted
# Algorithm: Dijkstra + Heap
# Time Complexity: O(
# Runtime: 88ms (top 11.0%)
# Intuition: 다익스트라와 같은 원리지만 path들을 저장해야 함. 그래서 min을 따진 뒤 업데이트 해주는게 아니라 전부 넣어준다.
#            내가 의아했던 부분은 i == dst 일 때 바로 p를 반환해버리는 점이었는데 (만약 뒤에 더 적은 price 값을 가진 i == dst 가 나오면?)
#            우선순위가 price가 작은 순이고, price는 계속 증가하므로(음수 엣지가 없으므로 절대 감소하지 않음)
#            i == dst 인 p들을 전부 저장한 뒤 min 을 찾지 않아도 맨 처음 나오는 p가 최솟값이라고 확신할 수 있다.
#            candidate 리스트를 만들어서 추가한 뒤 while문을 다 돌리고 min(cand)를 하면 타임아웃이 뜬다.






