# my solution
class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        from collections import defaultdict
        edges = defaultdict(list)
        l = len(arr)
        targets = []
        for i, value in enumerate(arr):
            if i + value < l:
                edges[i].append(i + value)
            if -l <= i - value < 0:
                edges[i].append(l + i - value)
            else:
                edges[i].append(i - value)
            if value == 0:
                targets.append(i)

        visited = [0] * l

        def bfs(idx, edges, visited):
            if visited[idx] == 0:
                visited[idx] = 1
                for node in edges[idx]:
                    bfs(node, edges, visited)

        bfs(start, edges, visited)
        if len(targets) == 0:
            return False

        for t in targets:
            if visited[t] == 1:
                return True

        return False

# Status: Wrong Answer
# Algorithm: BFS
# Time Complexity: O(N + E) (N: len of arr, E: num of edges)
# Runtime:
# Intuition: 방법은 맞는 것 같은데 한가지 케이스에서 에러가 난다. 흠 뭐가 문제일까?
#            그리고 value 0 인 모든 인덱스에 도달할 수 있는지 여부인 줄 알았는데 단 한개라도 도달할 수 있으면 True 인거였다.
#            그러면 이것보다 더 간단히 만들 수 있을 것 같다.
#            또한 문제의 조건, 모든 요소가 양수인 것을 이용해서 visited 를 만들 필요 없이 방문했던 인덱스의 value는 음수로 만들어주면 간편하다.


# leetcode solution
class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        if start < len(arr) and 0 <= arr[start]:
            if arr[start] == 0:
                return True
            self.canReach(arr, start - arr[start])
            self.canReach(arr, start + arr[start])
            arr[start] = -1
            return False
# Status: Accepted
# Algorithm: DFS
# Time Complexity: O(N)
# Runtime: 228ms (top 2.4%)



