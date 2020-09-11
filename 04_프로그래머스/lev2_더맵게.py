import heapq

def solution(scoville, K):
    heapq.heapify(scoville)
    count = 0
    while len(scoville) >= 2:
        if scoville[0] >= K:
            break

        fir = heapq.heappop(scoville)
        sec = heapq.heappop(scoville)
        heapq.heappush(scoville, fir + sec * 2)
        count += 1

    if scoville[0] < K:
        return -1
    return count
# Status: Accepted
# Time Complexity: O(n lg(n)
