# coding=utf-8
# my solution
import heapq

def solution(n, costs):
    # 인접행렬
    adj_mat = [[None] * n for _ in range(n)]
    for c in costs:
        adj_mat[c[0]][c[1]] = c[2]
        adj_mat[c[1]][c[0]] = c[2]

    visited = [False] * n
    heap = [(0, costs[0][0])]
    answer = 0
    # 코스트가 낮은 순으로 우선순위 큐
    while heap:
        point = heapq.heappop(heap)
        if visited[point[1]] is False:
            answer += point[0]
            visited[point[1]] = True
        for i, cost in enumerate(adj_mat[point[1]]):
            if visited[i] is False and cost:
                heapq.heappush(heap, (cost, i))

    return answer
# Status: Accepted
# Intuition: 우선순위큐를 사용하되, 힙에 추가할 때가 아니라 뺄 때 visited를 체크하는게 포인트 - 추가할 때 visited를 True로 바꾸면 코스트가 더 낮은 항이 아예 힙에 추가되지 않는 경우가 발생함.
# Note: 엄청 많이 헤맨 결과물이라, 코드가 지저분하다.
#       시간을 너무 많이 써서 코드 다듬고 다른사람들 코드 확인하는 건 다음번에~






