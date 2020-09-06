# 방향, 양수가중치 그래프 -> 다익스트라를 써보자
# 노드 갯수는 1이상 100이하
# 엣지 개수는 1이상 6000이하
# 한 엣지의 최대 가중치 값은 100

class Solution:
    def networkDelayTime(self, times: List[List[int]], N: int, K: int) -> int:
        completed = [0] * (N + 1)
        distance = [sys.maxsize] * (N + 1)

        from collections import defaultdict
        edges = defaultdict(list)

        for edge in times:
            edges[edge[0]].append((edge[1], edge[2]))

        for _ in range(100):
            completed[K] = 1
            for edge in edges[K]:
                target, weight = edge
                distance[target] = min(distance[K] + weight, distance[target])
            next_k = -1
            for edge in edges[K]:
                if completed[edge[0]] != 1:
                    if (0 <= next_k and distance[edge[0]] < distance[next_k]) or next_k == -1:
                        next_k = edge[0]
            if next_k == -1:
                break
            K = next_k

        if sum(completed) != len(completed) - 1:
            return -1
        else:
            return max(distance)
# Status: Wrong Answer
# Algorithm: Dijkstra
# Time Complexity:
# Runtime:
# Intuition: 다익스트라를 처음 써보는데 이것저것 보수하다보니 너무 지저분해졌다. 다시 한번 해보자-!


# my solution
class Solution:
    def networkDelayTime(self, times: List[List[int]], N: int, K: int) -> int:
        completed = [0] * (N + 1)
        dist = [sys.maxsize] * (N + 1)

        from collections import defaultdict
        edges = defaultdict(list)
        for edge in times:
            edges[edge[0]].append((edge[1], edge[2]))

        dist[K] = 0
        while True:
            for target, weight in edges[K]:
                dist[target] = min(dist[target], dist[K] + weight)
            completed[K] = 1
            next_k = -1
            for target in range(1, N + 1):
                if completed[target] != 1 and dist[target] != sys.maxsize:
                    if (0 <= next_k and dist[target] < dist[next_k]) or next_k < 0:
                        next_k = target
            if next_k < 0:
                break
            K = next_k

        if 0 in completed[1:]:
            return -1
        return max(dist[1:])
# Status: Accepted
# Algorithm: Dijkstra
# Time Complexity: O(N^2 + E) (E: num of edges) 
# Runtime: 488ms (top 15.8%)
# Intuitions: 위의 코드를 깔끔하게 정리하고 디버깅한 코드. next_k 설정하는 포문에서 생각해줘야할 조건이 꽤 있었다.
#             릿코드 솔루션을 보니 다익스트라에 힙을 사용해서 O(E logE)로 줄일 수 있던데 내일 해보자
