# my solution
class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        from collections import defaultdict
        status = defaultdict(int)
        self.visited = set()

        def bfs(idx):
            if status[idx] == 0:
                self.visited.add(idx)
                status[idx] = 1
                for neighbor in rooms[idx]:
                    bfs(neighbor)

        bfs(0)
        return len(self.visited) == len(rooms)
# Status: Accepted
# Algorithm: BFS
# Time Complexity: O(N + E) (N: num of rooms, E: num of keys(edges))
# Runtime: 60ms (top 2.5%)
# Intuition: 0에서부터 탐색을 진행하며 방문한 방들은 visited에 추가
#            탐색을 완료한 후 방문한 방 개수와 전체 방 개수가 같으면 True
#            사실 set이 아니라 list로 했어도 같았겠지만 의미를 명확히 하기 위해 set 사용